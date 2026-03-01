async function getCropPrediction(soilData) {
    const response = await fetch(
        'http://localhost:8000/api/ai/predict-single',
        {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(soilData)
        }
    );
    const result = await response.json();
    return result.predicted_crop;
}

module.exports = {
    getCropPrediction
};
