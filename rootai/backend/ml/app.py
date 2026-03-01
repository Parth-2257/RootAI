from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import pickle
import numpy as np
import pandas as pd
import io

app = FastAPI(title="RootAI Crop Prediction API")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"]
)

try:
    with open("minmaxscaler.pkl", "rb") as scaler_file:
        scaler = pickle.load(scaler_file)
    with open("model.pkl", "rb") as model_file:
        model = pickle.load(model_file)
    print("Models loaded successfully")
except Exception as e:
    print(f"Error loading models: {e}")

crop_dict = {
    1: 'rice', 2: 'maize', 3: 'chickpea',
    4: 'kidneybeans', 5: 'pigeonpeas', 6: 'mothbeans',
    7: 'mungbean', 8: 'blackgram', 9: 'lentil',
    10: 'pomegranate', 11: 'banana', 12: 'mango',
    13: 'grapes', 14: 'watermelon', 15: 'muskmelon',
    16: 'apple', 17: 'orange', 18: 'papaya',
    19: 'coconut', 20: 'cotton', 21: 'jute', 22: 'coffee'
}

@app.get("/")
def root():
    return {"message": "RootAI ML API is running"}

@app.post("/api/ai/upload-csv")
async def predict_from_csv(file: UploadFile = File(...)):
    try:
        contents = await file.read()
        df = pd.read_csv(io.StringIO(contents.decode("utf-8")))

        df.columns = df.columns.str.strip().str.lower()

        column_mapping = {
            'n': 'nitrogen',
            'p': 'phosphorus', 
            'k': 'potassium',
            'ph': 'ph',
            'humidity': 'moisture',
            'temperature': 'temperature',
            'rainfall': 'rainfall'
        }
        df.rename(columns=column_mapping, inplace=True)

        required_columns = [
            'nitrogen', 'phosphorus', 'potassium',
            'temperature', 'moisture', 'ph', 'rainfall'
        ]

        missing = [col for col in required_columns if col not in df.columns]
        if missing:
            raise HTTPException(
                status_code=400,
                detail=f"Missing columns: {missing}"
            )

        features = df[required_columns].values
        scaled_features = scaler.transform(features)
        predictions = model.predict(scaled_features)

        results = []
        for i, pred in enumerate(predictions):
            if isinstance(pred, (int, np.integer)):
                crop_name = crop_dict.get(int(pred), str(pred))
            else:
                crop_name = str(pred)

            row_data = df.iloc[i].to_dict()
            results.append({
                "row": i + 1,
                "nitrogen": float(row_data.get('nitrogen', 0)),
                "phosphorus": float(row_data.get('phosphorus', 0)),
                "potassium": float(row_data.get('potassium', 0)),
                "temperature": float(row_data.get('temperature', 0)),
                "moisture": float(row_data.get('moisture', 0)),
                "ph": float(row_data.get('ph', 0)),
                "rainfall": float(row_data.get('rainfall', 0)),
                "predicted_crop": crop_name
            })

        crop_counts = {}
        for r in results:
            crop = r['predicted_crop']
            crop_counts[crop] = crop_counts.get(crop, 0) + 1

        most_common_crop = max(crop_counts, key=crop_counts.get)

        avg_values = {
            "avg_nitrogen": float(df['nitrogen'].mean()),
            "avg_phosphorus": float(df['phosphorus'].mean()),
            "avg_potassium": float(df['potassium'].mean()),
            "avg_temperature": float(df['temperature'].mean()),
            "avg_moisture": float(df['moisture'].mean()),
            "avg_ph": float(df['ph'].mean()),
            "avg_rainfall": float(df['rainfall'].mean())
        }

        return {
            "success": True,
            "total_rows": len(results),
            "most_recommended_crop": most_common_crop,
            "crop_distribution": crop_counts,
            "averages": avg_values,
            "predictions": results
        }

    except HTTPException:
        raise
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/api/ai/predict-single")
async def predict_single(data: dict):
    try:
        input_data = np.array([[
            data.get('nitrogen', 0),
            data.get('phosphorus', 0),
            data.get('potassium', 0),
            data.get('temperature', 0),
            data.get('moisture', 0),
            data.get('ph', 0),
            data.get('rainfall', 100)
        ]])

        scaled = scaler.transform(input_data)
        prediction = model.predict(scaled)

        if isinstance(prediction[0], (int, np.integer)):
            crop_name = crop_dict.get(int(prediction[0]), str(prediction[0]))
        else:
            crop_name = str(prediction[0])

        return {
            "success": True,
            "predicted_crop": crop_name
        }

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
