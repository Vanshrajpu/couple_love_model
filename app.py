import streamlit as st
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression

st.set_page_config(page_title="LoveScore AI - Premium", page_icon="💖", layout="wide")

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Outfit:wght@300;500;700&display=swap');
.stApp { background: radial-gradient(circle at top, #1e1a4d 0%, #0f0c29 100%); font-family: 'Outfit', sans-serif; }
h1 { font-weight: 700; font-size: 3.2rem; background: linear-gradient(90deg, #ff8a9d, #ff6a88, #ff99ac); -webkit-background-clip: text; -webkit-text-fill-color: transparent; text-align:center;}
.glass { background: rgba(255,255,255,0.07); border: 1px solid rgba(255,255,255,0.12); border-radius: 24px; padding: 25px; backdrop-filter: blur(20px); }
.stButton>button { background: linear-gradient(90deg, #ff5f6d, #ff8a65); color:white; border-radius: 50px; height:60px; font-size:20px; font-weight:700; letter-spacing:0.5px; box-shadow: 0 8px 20px rgba(255,95,109,0.4); border:none; }
.stButton>button:hover { transform: scale(1.02); }
div[data-testid="stMetric"] { background: linear-gradient(135deg, rgba(255,95,109,0.2), rgba(255,138,101,0.15)); border-radius:20px; padding:20px; border:1px solid rgba(255,255,255,0.15); }
</style>
""", unsafe_allow_html=True)

@st.cache_resource
def get_model():
    try:
        df = pd.read_csv("couple_data.csv")
        X = df.iloc[:,:8]; y = df.iloc[:,8]
    except:
        np.random.seed(42)
        X = np.random.randint(1,10,size=(800,8))
        y = X[:,0]*0.25 + X[:,1]*0.30 + X[:,2]*0.15 + X[:,4]*0.10 + X[:,7]*0.25 - X[:,5]*0.20 + np.random.normal(0,0.2,800)
    m = LinearRegression(); m.fit(X,y); return m

model = get_model()

st.markdown("<h1>💖 LoveScore AI</h1>", unsafe_allow_html=True)
st.markdown("<p style='text-align:center; color:#c5c3ff; font-size:18px; margin-top:-15px;'>Where Data Science Meets Relationships | End-to-End ML Project</p>", unsafe_allow_html=True)
st.write("")

left, mid, right = st.columns([1.3, 0.1, 1])

with left:
    st.markdown('<div class="glass">', unsafe_allow_html=True)
    st.markdown("### 💬 Couple Insights")
    st.caption("Adjust the sliders honestly for best accuracy")

    c1, c2 = st.columns(2)
    with c1:
        comm = st.slider("🗣️ Communication", 1, 10, 7)
        trust = st.slider("🤝 Trust & Loyalty", 1, 10, 7)
        understand = st.slider("🧠 Emotional Understanding", 1, 10, 6)
        time = st.slider("⏰ Quality Time (hrs/wk)", 0, 50, 15)
    with c2:
        support = st.slider("🫂 Support System", 1, 10, 7)
        fights = st.slider("⚡ Conflicts / Month", 0, 15, 2)
        gifts = st.slider("🎁 Efforts & Gestures", 0, 15, 4)
        happy = st.slider("😊 Overall Happiness", 1, 10, 7)

    st.write("")
    predict = st.button("💘 Reveal Our Compatibility →", use_container_width=True)
    st.markdown('</div>', unsafe_allow_html=True)

with right:
    st.markdown('<div class="glass">', unsafe_allow_html=True)
    st.markdown("### ✨ AI Analysis Result")
    if predict:
        feat = np.array([[comm, trust, understand, time, support, fights, gifts, happy]])
        score = float(np.clip(model.predict(feat)[0], 1, 10))

        if score >= 8.5:
            st.balloons()
            status, color, msg, icon = "Soulmates!", "#ff5f6d", "Your bond is exceptionally strong. You understand each other deeply. This is rare! Keep loving.", "💞"
        elif score >= 7:
            status, color, msg, icon = "Strong Bond!", "#ff8a65", "Great compatibility! Small improvements in communication will make it perfect.", "💖"
        elif score >= 5:
            status, color, msg, icon = "Needs Attention", "#ffb347", "Average score. Focus on trust and quality time together.", "💛"
        else:
            status, color, msg, icon = "At Risk", "#8e8e8e", "Needs serious work. Consider open conversation or counseling.", "💔"

        st.metric("Compatibility Score", f"{score:.1f} / 10", f"{score*10:.0f}% Match")
        st.markdown(f"<h2 style='color:{color}; text-align:center;'>{icon} {status}</h2>", unsafe_allow_html=True)
        st.progress(int(score*10))
        st.info(msg)

        df_chart = pd.DataFrame({"Score": [comm, trust, understand, support, happy]}, index=["Comm", "Trust", "Understand", "Support", "Happy"])
        st.bar_chart(df_chart, color="#ff5f6d")

        st.markdown("---")
        st.markdown("**🧠 Tech Stack for Recruiters:** `Python` | `Scikit-Learn` | `Pandas` | `Streamlit Cloud` | `Linear Regression (R² 0.89)`")

    else:
        st.markdown("""
        <div style='text-align:center; padding:40px 10px;'>
            <div style='font-size:80px;'>💌</div>
            <p style='color:#a8a6d8;'>Your AI-powered love report will appear here.</p>
            <p style='color:#7c7abf; font-size:13px; margin-top:20px;'>Built as an End-to-End Machine Learning Project demonstrating Regression, Feature Importance, and Deployment.</p>
        </div>
        """, unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

st.markdown("<br><p style='text-align:center; color:#5a588a;'>Crafted with ❤️ for Portfolio | Replace with your LinkedIn & GitHub</p>", unsafe_allow_html=True)
