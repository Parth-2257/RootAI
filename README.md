# RootAI — Soil Health Dashboard from Sensor Logs

> A sensor-driven web system that processes soil sensor logs, visualizes soil health trends, detects threshold breaches, and recommends optimal planting windows.

---

## Table of Contents

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

## Problem Statement

Modern farms increasingly use sensors to monitor soil parameters such as pH, moisture, nitrogen levels, and temperature. However, raw sensor logs provide limited insight without structured analysis. Farmers need meaningful interpretation of soil health trends to determine planting windows and manage crop health proactively.

### The Problem

There is no structured tool that:

- Ingests time-series soil sensor data
- Tracks long-term soil health trends
- Detects threshold breaches
- Correlates soil parameters with historical yield data
- Provides actionable planting recommendations

Challenges include:

- Implementing time-series analysis
- Handling multi-parameter correlation
- Designing meaningful alert thresholds
- Avoiding false-positive alerts
- Raw data without interpretation limits practical value

### The Consequence

Without analytical dashboards:

- Soil degradation may go unnoticed
- Planting decisions are poorly timed
- Yield predictions are inaccurate
- Resource application becomes reactive
- Long-term soil health declines

Missed early signals reduce productivity and sustainability.

### The Challenge

Can we build a Soil Health Dashboard that:

- Processes sensor logs from CSV inputs
- Visualizes trends in soil parameters
- Detects critical threshold breaches
- Correlates soil conditions with historical yield
- Recommends optimal planting windows
- Provides clear, actionable alerts

The objective is to convert sensor data into meaningful agricultural intelligence.

### Target Users

| User Type | Description |
|---|---|
| Farmers | Primary beneficiaries for on-ground decision-making |
| Agricultural Consultants | Data-backed advisory services |
| Agri-tech Startups | Integration into existing platforms |
| Government Departments | Policy and analytics support |
| NGOs | Rural farming outreach programs |

---

## Solution Overview

RootAI is a full-stack web application that ingests soil sensor data exported as CSV files and processes it through a rule-based analysis engine. It presents meaningful agricultural intelligence through an interactive dashboard. Users can select a field, view soil health trends over time, receive threshold-based alerts, and get planting window recommendations — no laboratory input or machine learning required.

---

## Key Features

- **Multi-Field Data Support** — Dropdown-based field selection to load and analyze sensor logs per field
- **Soil Health Score (0–100)** — Rule-based scoring algorithm that evaluates soil parameters and outputs a normalized health score
- **Trend Visualization** — Per-field time-series charts for pH, moisture, nitrogen, temperature, and other parameters
- **Smart Alerts** — Threshold-based and trend-based alerts that flag anomalies and avoid false positives
- **Planting Window Recommendation** — Actionable recommendations on optimal planting periods based on current soil conditions

---

## System Architecture

```
Sensor --> CSV File --> Backend (Node.js + CSV Parser) --> Rule-Based algorithm --> Frontend Dashboard
```

### Components

**1. Frontend**
- Built with HTML, CSS, and JavaScript
- Field selection via dropdown
- Displays trend charts, health score, alerts, and planting recommendations
- Communicates with backend via REST API

**2. Backend**
- Built with Node.js and Express.js
- Reads and parses CSV files using a CSV parser library
- Runs rule-based logic for soil health scoring, alert detection, and planting window calculation
- Serves structured JSON responses to the frontend

**3. Data Layer (CSV)**
- Sensor data exported as CSV files
- Each file represents time-series readings for a field
- Parameters include: pH, moisture, nitrogen (N), phosphorus (P), potassium (K), temperature

**4. Database (MongoDB)**
- Stores parsed sensor records
- Stores computed health scores and alert logs
- Supports historical trend queries

---

## Technology Stack

| Layer | Technology |
|---|---|
| Frontend | HTML, CSS, JavaScript |
| Backend | Node.js, Express.js |
| Data Parsing | csv-parser (Node.js library) |
| Rule algorithm | Custom JavaScript logic |
| Database | MongoDB |
| Deployment | AWS / Render / Vercel *(to be finalized)* |

---

## End-to-End Workflow

1. Soil sensors collect field data and export it as a CSV file
2. CSV file is uploaded to the system via the dashboard
3. Backend parses and validates the incoming data
4. Rule-based engine evaluates soil parameters against defined thresholds
5. Soil health score (0–100) is calculated and classified
6. Crop recommendation logic runs based on current soil conditions
7. Results and sensor records are stored in MongoDB
8. API sends structured response back to the frontend
9. Dashboard renders health score, alerts, trends, and crop recommendations
10. Farmer reviews insights and makes informed planting decisions

---


## Team

| Member | Role | Responsibilities |
|---|---|---|
| Parth Nayak | Backend & System Architect |	API development, business logic integration, database schema design, server setup, deployment
| Aditya Singh Shekhawat | Algorithm & Logic Engineer | Soil health scoring, formulas, planting window|rule-based crop recommendation algorithm 
| Anuj Raghuwanshi | Frontend Developer | UI/UX design, trend charts, dashboard, API integration |

---

## Future Scope

The following features are planned for future expansion beyond the current build:

- Multi-Field Comparison Dashboard
- Yield Correlation Analysis
- PDF Export Reports
- AI-Powered Plain English Insights
- Weather Correlation algorithm
- SMS / WhatsApp Alerts
- Predictive Soil Forecasting
- Mobile application development
- Government-level agricultural analytics dashboard

---

## Known Limitations

- No real-time sensor integration → Users must manually enter soil values.
- Rule-based logic limitation → Fixed formulas may not work perfectly for every region or soil type.
- Fixed thresholds → Nutrient ranges are static, not dynamically optimized.
- Internet required → Cannot work offline.
- No authentication → Anyone can access and use it.
- No yield prediction → You recommend crops but don’t estimate production output.
---

## Impact

RootAI converts raw sensor logs into meaningful agricultural intelligence by:

- Enabling proactive soil health monitoring
- Improving timing of planting decisions
- Reducing soil degradation through early detection
- Supporting data-driven resource application
- Promoting sustainable and productive farming practices

RootAI aims to make smart farming accessible, affordable, and scalable.

---