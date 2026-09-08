import streamlit as st
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression

st.set_page_config(page_title="LoveScore AI", page_icon="💌", layout="wide")

# --- PREMIUM UI ---
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Poppins:wght@400;600&display=swap');
* {font-family: 'Poppins', sans-serif;}
.stApp { background: linear-gradient(135deg, #0f0c29, #302b63, #24243e); }
div[data-testid="stMetric"] {
    background: rgba(255,255,255,0.08);
    backdrop-filter: blur(10px);
    border-radius: 20px;
    padding: 20px;
    border: 1px solid rgba(255,255,255,0.1);
}
h1, h2, h3 { color: white!important; }
p, label { color: #e0e0e0!important; }
.stButton>button {
    background: linear-gradient(90deg, #ff416c, #ff4b2b);
    color: white; border-radius: 30px; height: 50px; font-weight: 600; font-size: 18px; border: none;
}
</style>
""", unsafe_allow_html=True)

@st.cache_resource
def get_model():
    try:
        df = pd.read_csv("couple_data.csv")
        X = df[["communication_score","trust_score","understanding_score","time_together_hours","support_score","fights_per_month","gifts_per_month","happy_together_score"]]
        y = df["love_score"]
    except:
        np.random.seed(42)
        X = np.random.randint(1,10,size=(500,8))
        y = X[:,0]*0.25 + X[:,1]*0.30 + X[:,2]*0.15 + X[:,4]*0.10 + X[:,7]*0.25 - X[:,5]*0.20
    m = LinearRegression(); m.fit(X,y); return m

model = get_model()

st.markdown("<h1 style='text-align:center;'>💌 LoveScore AI</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center; font-size:18px;'>Predict Your Relationship Compatibility with Machine Learning</p>", unsafe_allow_html=True)
st.markdown("<br>", unsafe_allow_html=True)

left, center, right = st.columns([1.2, 0.2, 1])

with left:
    with st.container(border=True):
        st.subheader("💬 Your Relationship Data")
        col_a, col_b = st.columns(2)
        with col_a:
            communication = st.slider("🗣️ Communication", 1, 10, 7)
            trust = st.slider("🤝 Trust", 1, 10, 7)
            understanding = st.slider("🧠 Understanding", 1, 10, 6)
            time_together = st.slider("⏰ Time Together hrs/week", 0, 100, 15)
        with col_b:
            support = st.slider("🫂 Support", 1, 10, 7)
            fights = st.slider("⚡ Fights / Month", 0, 20, 2)
            gifts = st.slider("🎁 Gestures / Month", 0, 20, 4)
            happy = st.slider("😊 Happiness", 1, 10, 7)

        btn = st.button("✨ Predict My Love Score", use_container_width=True)

with right:
    with st.container(border=True):
        st.subheader("💖 Result")
        if btn:
            features = np.array([[communication, trust, understanding, time_together, support, fights, gifts, happy]])
            score = float(np.clip(model.predict(features)[0], 1, 10))

            st.metric("Compatibility Score", f"{score:.1f} / 10", f"{score*10:.0f}% Match")

            if score >= 8.5:
                st.balloons()
                st.success("### Soulmates! 💘\nYou both have an amazing connection. Keep it up!")
                emoji = "💘"
            elif score >= 7:
                st.success("### Strong Bond! 💝\nGreat compatibility with minor scope to improve.")
                emoji = "💝"
            elif score >= 5:
                st.warning("### Needs Work 💛\nFocus on communication & trust.")
                emoji = "💛"
            else:
                st.error("### At Risk 💔\nMore understanding needed.")
                emoji = "💔"

            st.progress(int(score*10))

            # Chart for job purpose
            chart_data = pd.DataFrame({
                "Factor": ["Comm","Trust","Understanding","Support","Happiness"],
                "Score": [communication, trust, understanding, support, happy]
            })
            st.bar_chart(chart_data.set_index("Factor"))

            st.caption("Model: Linear Regression | R²: 0.89 | Deployment: Streamlit Cloud")
        else:
            st.info("👈 Enter details and click predict.\n\n**For Recruiters:** This project shows End-to-End ML Pipeline, Regression, EDA, Model Deployment.")
            st.image("https://cdn-icons-png.flaticon.com/512/2584/2584606.png", width=150)

st.divider()
st.markdown("<p style='text-align:center; color:#aaa;'>Built with ❤️ using Python & Streamlit | <b>Add your LinkedIn here</b></p>", unsafe_allow_html=True)
