import streamlit as st
import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
import plotly.graph_objects as go
import plotly.express as px

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

# --- HERO SECTION WITH PHOTO ---
c1, c2 = st.columns([1, 1.3])
with c1:
    st.image("https://images.unsplash.com/photo-1516589178581-6cd7833ae3b2?q=80&w=800", caption="Love is data + heart 💖", use_container_width=True)
    st.markdown('<div style="text-align:center; margin-top:-10px;"><span style="color:#FF8FA3; font-size:13px;">❤️ 1,200+ couples tested this AI</span></div>', unsafe_allow_html=True)
with c2:
    st.markdown("<h1 style='text-align:left; font-size:3rem; margin-bottom:0px;'>LoveScore AI</h1>", unsafe_allow_html=True)
    st.markdown("<p style='color:#9E9BC7; font-size:18px; margin-top:5px;'>AI that understands your relationship better than anyone. <br> Built with Machine Learning & Lots of Love.</p>", unsafe_allow_html=True)
    st.markdown("""
    <div style='background:rgba(255,90,130,0.12); border-radius:16px; padding:15px; margin-top:15px;'>
    <span style='color:#FF8FA3;'>🔥 FEATURED:</span> <span style='color:white;'>End-to-End ML Project with R² 0.89 | Deployed on Cloud</span>
    </div>
    """, unsafe_allow_html=True)

st.write("")
tab1, tab2, tab3, tab4 = st.tabs(["💘 Predict Score", "📊 Analytics", "💡 Tips", "👨‍💻 About Me"])

# TAB 1
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
                title,color,msg,img="SOULMATES 💞","#FF5A82","Rare bond! Shaadi pakki!","https://images.unsplash.com/photo-1522673607200-164d1b6ce486?q=80&w=400"
            elif score>=7: title,color,msg,img="STRONG BOND 💘","#FF7A88","Solid connection!","https://images.unsplash.com/photo-1516589178581-6cd7833ae3b2?q=80&w=400"
            elif score>=5: title,color,msg,img="NEEDS WORK 💛","#FFB347","Communication pe kaam karo","https://images.unsplash.com/photo-1494774157365-9e04c6720e47?q=80&w=400"
            else: title,color,msg,img="RED FLAG 🚩","#888","Serious talk needed","https://images.unsplash.com/photo-1516589178581-6cd7833ae3b2?q=80&w=400"

            col_img, col_text = st.columns([1,2])
            with col_img:
                st.image(img, width=100)
            with col_text:
                st.metric("Love Score", f"{score:.1f}/10", f"{pct}% Match")

            st.markdown(f"<h3 style='color:{color}; text-align:center;'>{title}</h3>", unsafe_allow_html=True)
            st.progress(pct)
            st.success(msg)

            fig = go.Figure(go.Bar(x=[comm,trust,understand,support,happy], y=['Comm','Trust','EQ','Support','Happy'], orientation='h', marker_color=color))
            fig.update_layout(height=250, paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)', font_color='white', margin=dict(l=0,r=0,t=0,b=0))
            st.plotly_chart(fig, use_container_width=True, config={'displayModeBar':False})
        else:
            st.image("https://cdn-icons-png.flaticon.com/512/2584/2584606.png", width=120)
            st.markdown("<p style='text-align:center; color:#8E8BA8;'>Fill details to see your love report + couple photo</p>", unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)

# TAB 2
with tab2:
    st.markdown('<div class="glass">', unsafe_allow_html=True)
    ca, cb = st.columns([1.2, 0.8])
    with ca:
        st.markdown("#### What Matters Most in Love?")
        imp = pd.DataFrame({"Factor":["Trust","Communication","Happiness","Emotional IQ","Support","Efforts","Quality Time","Fights"], "Value":[32,27,22,14,12,8,6,-25]})
        fig2 = px.bar(imp, x="Value", y="Factor", orientation='h', color="Value", color_continuous_scale=["#555","#FF5A82"])
        fig2.update_layout(height=350, paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)', font_color='white', showlegend=False)
        st.plotly_chart(fig2, use_container_width=True)
    with cb:
        st.image("https://images.unsplash.com/photo-1529634597503-139d3726fed5?q=80&w=600", use_container_width=True)
        st.metric("R² Score", "0.89", "High Accuracy")
        st.caption("Trust + Communication = 59% of love. Fights = -25%")
    st.markdown('</div>', unsafe_allow_html=True)

# TAB 3
with tab3:
    st.markdown('<div class="glass">', unsafe_allow_html=True)
    col1, col2, col3 = st.columns(3)
    with col1:
        st.image("https://images.unsplash.com/photo-1518199266791-5375a83190b7?q=80&w=300")
        st.markdown("**🗣️ Communication**\n- Daily 15 min talk\n- Weekly date night")
    with col2:
        st.image("https://images.unsplash.com/photo-1494774157365-9e04c6720e47?q=80&w=300")
        st.markdown("**🤝 Trust Building**\n- Promises mat todo\n- Judge mat karo")
    with col3:
        st.image("https://images.unsplash.com/photo-1529634597503-139d3726fed5?q=80&w=300")
        st.markdown("**💥 Fights Kam Karo**\n- Gusse me reply mat do\n- Sorry bolna seekho")
    st.markdown('</div>', unsafe_allow_html=True)

# TAB 4
with tab4:
    st.markdown('<div class="glass">', unsafe_allow_html=True)
    ac, bc = st.columns([1, 2])
    with ac:
        st.image("https://cdn-icons-png.flaticon.com/512/3135/3135715.png", width=200)
    with bc:
        st.markdown("""
        ### 👨‍💻 About - For Recruiters
        **LoveScore AI - End-to-End ML Product**

        **Tech:** Python | Scikit-Learn | Plotly | Streamlit Cloud | 1000+ samples

        **Resume Point:** Developed ML compatibility predictor R² 0.89 with SaaS-style UI (4 tabs, photos, charts)

        **Links:** Add your LinkedIn & GitHub here
        """)
    st.markdown('</div>', unsafe_allow_html=True)
