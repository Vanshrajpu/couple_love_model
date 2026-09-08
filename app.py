import streamlit as st
import joblib
import pandas as pd

# =====================================================
# PAGE CONFIG
# =====================================================

st.set_page_config(
    page_title="Couple Love Predictor",
    page_icon="💕",
    layout="centered"
)

# =====================================================
# CUSTOM CSS
# =====================================================

st.markdown("""
<style>

.stApp {
    background: linear-gradient(135deg, #0f172a, #1e1b4b, #4c1d95);
}

.main-title {
    text-align: center;
    font-size: 48px;
    font-weight: 800;
    color: white;
    margin-bottom: 5px;
}

.subtitle {
    text-align: center;
    color: #cbd5e1;
    font-size: 18px;
    margin-bottom: 30px;
}

.card {
    background: rgba(255,255,255,0.08);
    padding: 30px;
    border-radius: 25px;
    border: 1px solid rgba(255,255,255,0.15);
    box-shadow: 0 15px 40px rgba(0,0,0,0.35);
}

.result-card {
    background: rgba(255,255,255,0.10);
    padding: 30px;
    border-radius: 25px;
    text-align: center;
    margin-top: 25px;
    border: 1px solid rgba(255,255,255,0.2);
}

.result-title {
    color: white;
    font-size: 25px;
    font-weight: 700;
}

.love-score {
    font-size: 55px;
    font-weight: 900;
    margin: 10px;
}

.footer {
    text-align: center;
    color: #94a3b8;
    margin-top: 40px;
    font-size: 14px;
}

</style>
""", unsafe_allow_html=True)

# =====================================================
# LOAD MODEL
# =====================================================

model = joblib.load("model.pkl")

# =====================================================
# HEADER
# =====================================================

st.markdown(
    '<div class="main-title">💕 Couple Love Predictor</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">'
    'AI-powered relationship compatibility prediction'
    '</div>',
    unsafe_allow_html=True
)

st.success("🟢 Machine Learning Model Ready")

# =====================================================
# INPUT SECTION
# =====================================================

st.markdown('<div class="card">', unsafe_allow_html=True)

st.subheader("💑 Enter Couple Details")

col1, col2 = st.columns(2)

with col1:

    communication = st.slider(
        "💬 Communication Score",
        0, 100, 50
    )

    trust = st.slider(
        "🤝 Trust Score",
        0, 100, 50
    )

    understanding = st.slider(
        "🧠 Understanding Score",
        0, 100, 50
    )

    time_together = st.number_input(
        "⏰ Time Together (Hours)",
        min_value=0.0,
        max_value=24.0,
        value=5.0
    )

with col2:

    support = st.slider(
        "❤️ Support Score",
        0, 100, 50
    )

    fights = st.number_input(
        "😤 Fights Per Month",
        min_value=0,
        max_value=50,
        value=2
    )

    gifts = st.number_input(
        "🎁 Gifts Per Month",
        min_value=0,
        max_value=50,
        value=1
    )

    happy_together = st.slider(
        "😊 Happy Together Score",
        0, 100, 50
    )

st.markdown("</div>", unsafe_allow_html=True)

# =====================================================
# PREDICTION BUTTON
# =====================================================

st.write("")

if st.button(
    "💕 Predict Love Score",
    use_container_width=True
):

    # Create input DataFrame
    input_data = pd.DataFrame([{
        "communication_score": communication,
        "trust_score": trust,
        "understanding_score": understanding,
        "time_together_hours": time_together,
        "support_score": support,
        "fights_per_month": fights,
        "gifts_per_month": gifts,
        "happy_together_score": happy_together
    }])

    # Prediction
    prediction = model.predict(input_data)[0]

    # Keep score between 0 and 100
    prediction = max(0, min(100, prediction))

    # =================================================
    # RESULT
    # =================================================

    st.markdown(
        '<div class="result-card">',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="result-title">💖 Predicted Love Score</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        f'<div class="love-score">💕 {prediction:.2f}/100</div>',
        unsafe_allow_html=True
    )

    # Message based on score

    if prediction >= 80:
        message = "💖 Excellent Compatibility!"
    elif prediction >= 60:
        message = "🥰 Strong Relationship!"
    elif prediction >= 40:
        message = "😊 Good Compatibility!"
    else:
        message = "💙 There is room to grow together!"

    st.subheader(message)

    st.markdown(
        "✨ Prediction generated using Linear Regression",
    )

    st.markdown("</div>", unsafe_allow_html=True)

# =====================================================
# FOOTER
# =====================================================

st.markdown(
    '<div class="footer">'
    'Built with Python • Pandas • Scikit-learn • Streamlit'
    '</div>',
    unsafe_allow_html=True
)
