# 🌱 RootAI — AI-Driven Soil Health Analysis & Smart Crop Recommendation

> An AI-powered web system that analyzes soil parameters to predict soil health and recommend the most suitable crops for maximum yield.

---

## 📌 Table of Contents

- [Problem Statement](#problem-statement)
- [Solution Overview](#solution-overview)
- [Key Features](#key-features)
- [System Architecture](#system-architecture)
- [Technology Stack](#technology-stack)
- [End-to-End Workflow](#end-to-end-workflow)
- [API Documentation](#api-documentation)
- [Module-wise Development](#module-wise-development)
- [Team](#team)
- [Future Scope](#future-scope)
- [Known Limitations](#known-limitations)
- [Impact](#impact)

---

## 🚜 Problem Statement

Agriculture productivity heavily depends on soil quality. However, most farmers lack access to affordable, real-time soil analysis systems. Traditional soil testing is costly, time-consuming, and requires laboratory infrastructure — leading to crop decisions based on assumptions rather than data. This results in:

- Low crop yield
- Soil degradation
- Economic losses for farmers

**RootAI** bridges this gap with an accessible, AI-powered soil health prediction and crop recommendation system.

### 🎯 Target Users

| User Type | Description |
|---|---|
| Farmers | Primary beneficiaries for on-ground decision-making |
| Agricultural Consultants | Data-backed advisory services |
| Agri-tech Startups | Integration into existing platforms |
| Government Departments | Policy and analytics support |
| NGOs | Rural farming outreach programs |

---

## 💡 Solution Overview

RootAI is a full-stack AI-based web application. Users input soil parameters through the frontend; the backend processes the input and passes it to a trained ML model that predicts:

- **Soil health classification**
- **Recommended crops for maximum yield**

Results are displayed instantly and optionally stored for analytics.

---

## ✨ Key Features

- 🧪 Soil health classification
- 🌾 Intelligent crop recommendation
- ⚡ Real-time prediction
- 🖥️ Clean, user-friendly UI
- 📊 Prediction history storage
- 🔌 Scalable backend design
- 📡 Future-ready IoT integration capability

---

## 🏗️ System Architecture

```
User → Frontend → Backend API → ML Model → Database → Response
```

### Components

**1. Frontend**
- Built with HTML, CSS, and JavaScript
- Collects soil parameters via input forms
- Sends data to backend via REST API
- Displays prediction results dynamically

**2. Backend**
- Built with Node.js and Express.js
- Handles API requests and input validation
- Communicates with ML model
- Stores inputs and predictions in database

**3. ML Model**
- Developed in Python using Scikit-learn
- Trained on soil dataset
- Outputs soil health status and crop recommendation

**4. Database (MongoDB)**
- Stores user input data
- Stores prediction results
- Logs and analytics

---

## 🛠️ Technology Stack

| Layer | Technology |
|---|---|
| Frontend | HTML, CSS, JavaScript |
| Backend | Node.js, Express.js |
| ML / AI | Python, Scikit-learn |
| Database | MongoDB |
| Deployment | AWS / Render / Vercel *(to be finalized)* |

---

## 🔄 End-to-End Workflow

1. User enters soil parameters (N, P, K, pH, moisture, temperature, etc.)
2. Frontend sends data via `POST` request to backend API
3. Backend validates the input
4. Backend forwards input to the ML model
5. Model generates prediction
6. Backend stores data in MongoDB
7. Prediction result is returned to frontend
8. User views soil health status and recommended crop

---

## 📡 API Documentation

> *Full API documentation to be completed.*

**Base URL:** `http://localhost:5000/api`

| Method | Endpoint | Description |
|---|---|---|
| POST | `/predict` | Submit soil parameters and get prediction |
| GET | `/history` | Retrieve past predictions |

**Sample Request Body:**
```json
{
  "nitrogen": 90,
  "phosphorus": 42,
  "potassium": 43,
  "ph": 6.5,
  "moisture": 82,
  "temperature": 23.5
}
```

**Sample Response:**
```json
{
  "soil_health": "Good",
  "recommended_crop": "Rice",
  "confidence": 0.91
}
```

---

## 📦 Module-wise Development

### Checkpoint 1: Research & Planning
- Problem statement finalization
- Literature research
- Dataset identification
- Architecture planning
- Git repository setup

### Checkpoint 2: Backend Development
- REST API creation
- Data validation middleware
- MongoDB integration
- Prediction endpoint
- Unit testing

### Checkpoint 3: Frontend Development
- Responsive UI
- Soil input form
- Result display dashboard
- API integration

### Checkpoint 4: Model Training
- Data preprocessing
- Feature engineering
- Model training & evaluation
- Model serialization (`.pkl` file)

### Checkpoint 5: Model Integration
- Backend-to-model integration
- Prediction pipeline testing
- End-to-end validation

### Checkpoint 6: Deployment
- Backend & frontend hosting
- Model deployment
- Public live link
- Final system testing

---

## 👥 Team

| Member | Role | Responsibilities |
|---|---|---|
| Member 1 | Backend & Integration | API development, database management, ML integration |
| Member 2 | ML Engineer | Dataset preprocessing, model training, evaluation |
| Member 3 | Frontend Developer | UI/UX design, frontend logic, API integration |

---

## 🚀 Future Scope

**Short-Term**
- Fertilizer recommendation system
- Improved model accuracy with larger datasets
- Multilingual support
- User authentication & personal dashboard

**Long-Term**
- IoT sensor integration for real-time soil monitoring
- Mobile application development
- Satellite imagery integration
- Government-level agricultural analytics dashboard
- Yield estimation prediction
- AI-driven climate-adaptive farming suggestions

---

## ⚠️ Known Limitations

- Accuracy depends on dataset quality
- Manual input required (no live sensor data yet)
- Limited regional dataset coverage
- Internet connection required
- Initial model may not generalize globally

---

## 🌍 Impact

RootAI empowers farmers with data-driven decision-making by:

- ✅ Improving crop yield
- ✅ Reducing soil degradation
- ✅ Promoting sustainable farming practices
- ✅ Increasing farmer income
- ✅ Encouraging AI adoption in agriculture

> **RootAI aims to make smart farming accessible, affordable, and scalable. 🌱**

---

## 📄 License

This project is developed as part of a hackathon. License details to be added.
