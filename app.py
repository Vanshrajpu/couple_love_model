import streamlit as st
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression

st.title("Couple Love Score Predictor ❤️")

# Training data - yahi pe model ban jayega, pkl nahi chahiye
@st.cache_resource
def get_model():
    # Agar tere paas csv hai to yaha naam badal de, warna ye dummy data se bhi kaam chalega
    # Lekin best hai apna csv ka link de
    try:
        df = pd.read_csv("couple_data.csv") # agar csv repo me hai to
        X = df[["communication_score","trust_score","understanding_score","time_together_hours","support_score","fights_per_month","gifts_per_month","happy_together_score"]]
        y = df["love_score"]
    except:
        # Fallback - agar csv nahi mila to tere 0.89 wale model jaisa data
        np.random.seed(42)
        X = np.random.randint(1, 10, size=(200, 8))
        y = X[:,0]*0.3 + X[:,1]*0.3 + X[:,2]*0.2 + X[:,4]*0.1 - X[:,5]*0.2 + X[:,7]*0.2
    model = LinearRegression()
    model.fit(X, y)
    return model

model = get_model()

communication = st.slider("Communication Score", 1, 10, 5)
trust = st.slider("Trust Score", 1, 10, 5)
understanding = st.slider("Understanding Score", 1, 10, 5)
time_together = st.number_input("Time Together Hours", 0, 100, 10)
support = st.slider("Support Score", 1, 10, 5)
fights = st.number_input("Fights Per Month", 0, 30, 2)
gifts = st.number_input("Gifts Per Month", 0, 30, 2)
happy = st.slider("Happy Together Score", 1, 10, 5)

if st.button("Predict Love Score"):
    features = np.array([[communication, trust, understanding, time_together, support, fights, gifts, happy]])
    prediction = model.predict(features)
    score = max(1, min(10, prediction[0]))
    st.success(f"Predicted Love Score: {score:.2f} ❤️")
