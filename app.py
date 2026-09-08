import streamlit as st
import pickle
import numpy as np
import os

# Sahi path - tere repo ke hisab se
model_path = "couple_love_model/couple_love_model.pkl"

# Model load
with open(model_path, "rb") as f:
    model = pickle.load(f)

st.title("Couple Love Score Predictor ❤️")

# Input - ISI ORDER ME LENA HAI
communication = st.slider("Communication Score", 1, 10, 5)
trust = st.slider("Trust Score", 1, 10, 5)
understanding = st.slider("Understanding Score", 1, 10, 5)
time_together = st.number_input("Time Together Hours", 0, 100, 10)
support = st.slider("Support Score", 1, 10, 5)
fights = st.number_input("Fights Per Month", 0, 30, 2)
gifts = st.number_input("Gifts Per Month", 0, 30, 2)
happy = st.slider("Happy Together Score", 1, 10, 5)

if st.button("Predict Love Score"):
    # IMPORTANT: Order wahi jo training me tha
    features = np.array([[communication, trust, understanding, time_together, support, fights, gifts, happy]])
    prediction = model.predict(features)
    st.success(f"Predicted Love Score: {prediction[0]:.2f}")
