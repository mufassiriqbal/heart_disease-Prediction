import streamlit as st
import pickle
import numpy as np

# Loadi trained model
with open("all_models.pkl", "rb") as f:
    all_models = pickle.load(f)


model = all_models[0]

st.set_page_config(page_title="Heart Disease Prediction", page_icon="❤️", layout="centered")

st.title("❤️ Heart Disease Prediction App")
st.write("Enter patient details below to check the risk of heart disease.")

# Input fields (example: adjust based on your dataset features)
age = st.number_input("Age", min_value=1, max_value=120, value=30)
sex = st.selectbox("Sex (0 = Female, 1 = Male)", [0, 1])
cp = st.selectbox("Chest Pain Type (0–3)", [0, 1, 2, 3])
trestbps = st.number_input("Resting Blood Pressure (mm Hg)", min_value=80, max_value=200, value=120)
chol = st.number_input("Cholesterol (mg/dl)", min_value=100, max_value=600, value=200)
fbs = st.selectbox("Fasting Blood Sugar > 120 mg/dl (1 = True, 0 = False)", [0, 1])
restecg = st.selectbox("Resting ECG (0–2)", [0, 1, 2])
thalach = st.number_input("Max Heart Rate Achieved", min_value=60, max_value=220, value=150)
exang = st.selectbox("Exercise Induced Angina (1 = Yes, 0 = No)", [0, 1])
oldpeak = st.number_input("ST Depression (Oldpeak)", min_value=0.0, max_value=10.0, value=1.0, step=0.1)
slope = st.selectbox("Slope of ST Segment (0–2)", [0, 1, 2])
ca = st.selectbox("Number of Major Vessels (0–3)", [0, 1, 2, 3])
thal = st.selectbox("Thalassemia (1 = Normal, 2 = Fixed Defect, 3 = Reversible Defect)", [1, 2, 3])


if st.button("Predict"):
    input_data = np.array([[age, sex, cp, trestbps, chol, fbs,
                            restecg, thalach, exang, oldpeak,
                            slope, ca, thal]])

    prediction = model.predict(input_data)[0]

    if prediction == 1:
        st.error("🚨 High chance of Heart Disease")
    else:
        st.success("✅ No Heart Disease Risk Detected")

st.markdown("---")
