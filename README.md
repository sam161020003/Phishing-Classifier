# 🛡️ Phishing Classifier

A machine learning pipeline for classifying websites as **phishing** or **legitimate**, using supervised learning on structured URL features. The project includes data preprocessing, model training with a Random Forest classifier, evaluation, and model serialization.

---

## 📌 Objective

To build a reliable classifier that can distinguish phishing websites from legitimate ones using extracted features from website URLs.

---

## 🧠 Project Overview

This project does the following:
- Loads a phishing dataset from a CSV file
- Preprocesses the data (handles missing values, encodes categorical features, scales numerics)
- Trains a **Random Forest** classifier
- Evaluates model accuracy
- Saves the trained model using `joblib`

---

## 📁 Project Structure


---
phishing-classifier/
│
├── data/
│ └── raw/ # Contains the raw CSV file (e.g., phishing_data.csv)
│
├── src/
│ ├── load_data.py # Loads the dataset
│ ├── preprocessing.py # Handles preprocessing steps
│ ├── train_model.py # Trains and evaluates the model
│ └── save_model.py # Saves the trained model
│
├── outputs/
│ └── model.joblib # Saved trained model
│
├── main.py # Runs the complete pipeline
├── requirements.txt # Python dependencies
└── README.md # Project documentation (this file)
