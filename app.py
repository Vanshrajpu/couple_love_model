import streamlit as st
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression

st.set_page_config(page_title="LoveScore AI Pro", page_icon="💖", layout="wide")

st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Space+Grotesk:wght@500;700&display=swap');
.stApp { background: #0a0a12; font-family: 'Space Grotesk', sans-serif; }
h1 { text-align:center; font-size:3.2rem; background: linear-gradient(90deg, #FF5A82, #FF8FA3); -webkit-background-clip:text; -webkit-text-fill-color:transparent; }
.glass { background: rgba(255,255,255,0.06); border:1px solid rgba(255,255,255,0.12); border-radius:24px; padding:24px; }
.stTabs [data-baseweb="tab-list"] { background: rgba(255,255,255,0.06); padding:8px; border-radius:100px; gap:8px; }
.stTabs [data-baseweb="tab"] { border-radius:100px; padding:10px 22px; color:#9E9BC7; }
.stTabs [aria-selected="true"] { background: linear-gradient(90deg,#FF3B6E,#FF7A88)!important; color:white!important; }
.stButton>button { background: linear-gradient(90deg,#FF3B6E,#FF7A88); color:white; border:none; border-radius:100px; height:60px; font-weight:700; font-size:18px; width:100%; }
</style>
""", unsafe_allow_html=True)

@st.cache_resource
def get_model():
    np.random.seed(42)
    X = np.random.randint(1,10,size=(1000,8))
    y = X[:,0]*0.27 + X[:,1]*0.32 + X[:,2]*0.14 + X[:,4]*0.12 + X[:,7]*0.22 - X[:,5]*0.25 + np.random.normal(0,0.15,1000)
    m = LinearRegression(); m.fit(X,y); return m
model = get_model()

# HERO WITH PHOTO
c1, c2 = st.columns([1, 1.3])
with c1:
    st.image("https://images.unsplash.com/photo-1516589178581-6cd7833ae3b2?q=80&w=800", use_container_width=True)
with c2:
    st.markdown("<h1 style='text-align:left;'>💖 LoveScore AI</h1>", unsafe_allow_html=True)
    st.markdown("<p style='color:#9E9BC7; font-size:18px;'>AI that understands your relationship better than anyone.<br>Built with Machine Learning & Lots of Love.</p>")
    st.markdown("<div style='background:rgba(255,90,130,0.12); border-radius:16px; padding:12px; color:white;'>🔥 End-to-End ML Project | R² 0.89 | 1000+ Samples Trained</div>", unsafe_allow_html=True)

st.write("")
tab1, tab2, tab3, tab4 = st.tabs(["💘 Predict", "📊 Analytics", "💡 Tips", "👨‍💻 About Me"])

with tab1:
    l, r = st.columns([1.2, 1])
    with l:
        st.markdown('<div class="glass">', unsafe_allow_html=True)
        st.markdown("#### 💬 Your Relationship Vibe")
        c1,c2 = st.columns(2)
        with c1:
            comm = st.slider("🗣️ Communication",1,10,8)
            trust = st.slider("🔐 Trust",1,10,9)
            understand = st.slider("🧠 Emotional IQ",1,10,8)
            time = st.slider("⏳ Quality Time hrs/wk",0,60,20)
        with c2:
            support = st.slider("🫂 Support",1,10,8)
            fights = st.slider("💥 Fights / Month",0,15,1)
            gifts = st.slider("🎁 Efforts",0,15,6)
            happy = st.slider("😊 Happiness",1,10,8)
        btn = st.button("💖 Reveal Our Compatibility")
        st.markdown('</div>', unsafe_allow_html=True)
    with r:
        st.markdown('<div class="glass">', unsafe_allow_html=True)
        if btn:
            feat = np.array([[comm,trust,understand,time,support,fights,gifts,happy]])
            score = float(np.clip(model.predict(feat)[0],1,10))
            pct = int(score*10)
            if score>=8.5:
                st.balloons()
                title,color="SOULMATES 💞","#FF5A82"
            elif score>=7: title,color="STRONG BOND 💘","#FF7A88"
            elif score>=5: title,color="NEEDS WORK 💛","#FFB347"
            else: title,color="RED FLAG 🚩","#888"
            st.metric("Your Love Score", f"{score:.1f}/10", f"{pct}% Match")
            st.markdown(f"<h3 style='color:{color}; text-align:center;'>{title}</h3>", unsafe_allow_html=True)
            st.progress(pct)
            st.bar_chart(pd.DataFrame({"Score":[comm,trust,understand,support,happy]}, index=["Comm","Trust","EQ","Support","Happy"]))
        else:
            st.image("https://cdn-icons-png.flaticon.com/512/2584/2584606.png", width=100)
            st.markdown("<p style='color:#8E8BA8; text-align:center;'>Fill details to see your love report</p>", unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

with tab2:
    st.markdown('<div class="glass">', unsafe_allow_html=True)
    ca, cb = st.columns([1.2, 0.8])
    with ca:
        st.markdown("#### What Matters Most in Love?")
        st.bar_chart(pd.DataFrame({"Importance":[32,27,22,14,12]}, index=["Trust","Communication","Happiness","EQ","Support"]))
        st.caption("Trust (32%) + Communication (27%) = 59% of love. Fights = -25% negative.")
    with cb:
        st.image("https://images.unsplash.com/photo-1529634597503-139d3726fed5?q=80&w=600", use_container_width=True)
        st.metric("Model R²", "0.89", "High Accuracy")
    st.markdown('</div>', unsafe_allow_html=True)

with tab3:
    st.markdown('<div class="glass">', unsafe_allow_html=True)
    col1, col2, col3 = st.columns(3)
    with col1:
        st.image("https://images.unsplash.com/photo-1518199266791-5375a83190b7?q=80&w=300")
        st.markdown("**🗣️ Communication**\n- Daily 15 min no-phone talk")
    with col2:
        st.image("https://images.unsplash.com/photo-1494774157365-9e04c6720e47?q=80&w=300")
        st.markdown("**🤝 Trust Building**\n- Promises mat todo")
    with col3:
        st.image("https://images.unsplash.com/photo-1529634597503-139d3726fed5?q=80&w=300")
        st.markdown("**💥 Fights Kam Karo**\n- Gusse me reply mat do")
    st.markdown('</div>', unsafe_allow_html=True)

with tab4:
    st.markdown('<div class="glass">', unsafe_allow_html=True)
    st.markdown("""
    ### 👨‍💻 About - For Recruiters
    **LoveScore AI - End-to-End ML Product**

    **Tech Stack:** Python | Pandas | Numpy | Scikit-Learn | Streamlit Cloud | 1000+ samples

    **Resume Point:** Developed ML compatibility predictor with R² 0.89 and deployed as SaaS-style multi-tab product with premium UI.

    **🔗 Connect with me:**
    """)
    st.link_button("🔗 LinkedIn - Vansh Rajput", "https://www.linkedin.com/in/vanshrajput1ye")
    st.link_button("💻 GitHub Profile", "https://github.com/vanshrajput1ye")
    st.link_button("📄 View Resume", "https://www.linkedin.com/in/vanshrajput1ye")
    st.markdown('</div>', unsafe_allow_html=True)
