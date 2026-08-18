# ============================================
# Wildfire Prediction System - Complete App
# ไฟล์นี้ต้องวางทับ app.py ทั้งไฟล์
# ============================================

# ========== IMPORTS (ต้องอยู่ด้านบนสุด) ==========
import streamlit as st
import pandas as pd
import numpy as np
import joblib
import json
import os
import matplotlib.pyplot as plt

# ========== PAGE CONFIG ==========
st.set_page_config(
    page_title="Wildfire Prediction",
    page_icon="🔥",
    layout="wide"
)

# ========== TITLE ==========
st.title("🔥 Wildfire Prediction System")
st.markdown("---")

# ========== SIDEBAR INPUT ==========
st.sidebar.header("📊 Input Parameters")

def user_input_features():
    X = st.sidebar.slider('X Coordinate', 1, 9, 5)
    Y = st.sidebar.slider('Y Coordinate', 2, 9, 5)
    month = st.sidebar.selectbox('Month', range(1, 13))
    day = st.sidebar.selectbox('Day of Week', range(1, 8))
    FFMC = st.sidebar.slider('FFMC Index', 0.0, 100.0, 50.0)
    DMC = st.sidebar.slider('DMC Index', 0.0, 300.0, 100.0)
    DC = st.sidebar.slider('DC Index', 0.0, 900.0, 400.0)
    ISI = st.sidebar.slider('ISI Index', 0.0, 60.0, 10.0)
    temp = st.sidebar.slider('Temperature (°C)', 0.0, 40.0, 20.0)
    RH = st.sidebar.slider('Relative Humidity (%)', 0, 100, 50)
    wind = st.sidebar.slider('Wind Speed (km/h)', 0.0, 10.0, 3.0)
    rain = st.sidebar.slider('Rain (mm/m²)', 0.0, 10.0, 0.0)
    
    data = {
        'X': X, 'Y': Y, 'month': month, 'day': day,
        'FFMC': FFMC, 'DMC': DMC, 'DC': DC, 'ISI': ISI,
        'temp': temp, 'RH': RH, 'wind': wind, 'rain': rain
    }
    return pd.DataFrame(data, index=[0])

input_df = user_input_features()

st.subheader("📋 Input Parameters")
st.write(input_df)

# ========== LOAD MODEL ==========
@st.cache_resource
def load_model():
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    model_path = os.path.join(BASE_DIR, 'best_model_joblib.pkl')
    scaler_path = os.path.join(BASE_DIR, 'scaler.pkl')
    features_path = os.path.join(BASE_DIR, 'features.json')
    
    if not os.path.exists(model_path):
        raise FileNotFoundError(f"Model file not found: {model_path}")
    if not os.path.exists(scaler_path):
        raise FileNotFoundError(f"Scaler file not found: {scaler_path}")
    
    model = joblib.load(model_path)
    scaler = joblib.load(scaler_path)
    
    features = None
    if os.path.exists(features_path):
        with open(features_path, 'r') as f:
            features = json.load(f)
    
    return model, scaler, features

# ========== PREDICTION ==========
try:
    model, scaler, features = load_model()
    
    st.subheader(" Prediction Result")
    
    if st.button(" Predict Burned Area", type="primary"):
        input_scaled = scaler.transform(input_df)
        prediction_log = model.predict(input_scaled)
        prediction = np.expm1(prediction_log[0])
        
        col1, col2, col3 = st.columns(3)
        
        with col1:
            st.metric("Predicted Area (hectares)", f"{prediction:.4f}")
        
        with col2:
            if prediction == 0:
                risk = "No Fire 🟢"
            elif prediction < 1:
                risk = "Low Risk 🟡"
            elif prediction < 10:
                risk = "Medium Risk 🟠"
            else:
                risk = "High Risk 🔴"
            st.metric("Risk Level", risk)
        
        with col3:
            st.metric("Log(Area+1)", f"{prediction_log[0]:.4f}")
        
        st.markdown("---")
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("### 📊 Predicted Area")
            fig, ax = plt.subplots(figsize=(6, 4))
            ax.bar(['Predicted Area'], [prediction], color='orange', edgecolor='black')
            ax.set_ylabel('Area (hectares)')
            ax.set_title('Predicted Burned Area')
            plt.tight_layout()
            st.pyplot(fig)
            plt.close(fig)
        
        with col2:
            if features and hasattr(model, 'feature_importances_'):
                st.markdown("### 🎯 Feature Importance")
                importance_df = pd.DataFrame({
                    'Feature': features,
                    'Importance': model.feature_importances_
                }).sort_values('Importance', ascending=True)
                
                fig, ax = plt.subplots(figsize=(6, 4))
                ax.barh(importance_df['Feature'], importance_df['Importance'], 
                       color='steelblue', edgecolor='black')
                ax.set_xlabel('Importance')
                ax.set_title('Feature Importance')
                plt.tight_layout()
                st.pyplot(fig)
                plt.close(fig)

except FileNotFoundError as e:
    st.error(f"❌ {str(e)}")
    st.info("💡 กรุณาตรวจสอบว่าไฟล์โมเดลถูกอัพโหลดขึ้น GitHub แล้ว")
except Exception as e:
    st.error(f"❌ เกิดข้อผิดพลาด: {str(e)}")

# ========== DEVELOPER SECTION (ส่วนผู้พัฒนา) ==========
st.markdown("---")
st.subheader("👨‍💻 ผู้พัฒนา (Developer)")

# ⚠️ แก้ไขข้อมูลส่วนตัวตรงนี้
dev_name = "นาพีรพัฒน์ กองบุตร"
dev_role = "ผู้พัฒนา"
dev_institution = "มหาวิทยาลัยราชภัฏนครปฐม"
dev_github = "https://github.com/664245025"

# โหลดรูปผู้พัฒนา
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
image_path = os.path.join(BASE_DIR, 'img', 'mark.jpg')

# Custom CSS
st.markdown("""
<style>
    .developer-card {
        background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
        padding: 2rem;
        border-radius: 15px;
        color: white;
        margin: 1rem 0;
        box-shadow: 0 4px 15px rgba(0,0,0,0.2);
    }
    .info-box {
        background: #f8f9fa;
        padding: 1.5rem;
        border-radius: 10px;
        border-left: 4px solid #667eea;
        margin: 1rem 0;
    }
    .tech-badge {
        display: inline-block;
        background: #667eea;
        color: white;
        padding: 0.3rem 0.8rem;
        border-radius: 20px;
        margin: 0.2rem;
        font-size: 0.85rem;
    }
</style>
""", unsafe_allow_html=True)

# แสดง Developer Card พร้อมรูป
col_img, col_info = st.columns([1, 3])

with col_img:
    if os.path.exists(image_path):
        st.image(
            image_path,
            caption=f" {dev_name}",
            width=200
        )
    else:
        st.markdown("<div style='font-size: 120px; text-align: center;'>👨‍💻</div>", unsafe_allow_html=True)
        st.info("💡 อัพโหลดรูปไปที่ `images/developer.jpg`")

with col_info:
    st.markdown(f"""
    <div class="developer-card">
        <h2 style="margin: 0;">{dev_name}</h2>
        <p style="margin: 0.5rem 0; font-size: 1.2rem; opacity: 0.9;">{dev_role}</p>
        <p style="margin: 0.3rem 0; opacity: 0.8;">🏫 {dev_institution}</p>
        <p style="margin: 0.3rem 0; opacity: 0.8;">📅 ปีการศึกษา 2026</p>
        <p style="margin: 0.3rem 0; opacity: 0.8;">📧 {dev_email}</p>
    </div>
    """, unsafe_allow_html=True)

# ข้อมูลโปรเจค
st.markdown("""
<div class="info-box">
    <h4>🔥 Wildfire Prediction System</h4>
    <p>โปรเจคนี้พัฒนาขึ้นเพื่อทำนายพื้นที่ที่ถูกไฟป่าโดยใช้ Machine Learning 
    โดยอาศัยข้อมูลทางอุตุนิยมวิทยาและดัชนีความเสี่ยงไฟป่า (Fire Weather Index) 
    จาก UCI Forest Fires Dataset</p>
</div>
""", unsafe_allow_html=True)

# เทคโนโลยีที่ใช้
st.subheader("🛠️ เทคโนโลยีที่ใช้")
tech_cols = st.columns(4)

with tech_cols[0]:
    st.markdown("**🐍 Programming**\n- Python 3.12\n- Pandas\n- NumPy")
with tech_cols[1]:
    st.markdown("**🤖 Machine Learning**\n- Scikit-Learn\n- XGBoost\n- Joblib")
with tech_cols[2]:
    st.markdown("**📊 Visualization**\n- Matplotlib\n- Seaborn")
with tech_cols[3]:
    st.markdown("**🌐 Web Framework**\n- Streamlit\n- GitHub")

# ขั้นตอนการพัฒนา
st.subheader("📝 ขั้นตอนการพัฒนา")
st.markdown("""
1. **📊 Data Collection** - รวบรวม dataset จาก UCI Machine Learning Repository
2. **🧹 Data Preprocessing** - ทำความสะอาดข้อมูล, แปลง categorical variables, log transform
3. **🤖 Model Development** - สร้างและเปรียบเทียบหลาย ML algorithms
4. ** Hyperparameter Tuning** - ปรับแต่งพารามิเตอร์ด้วย RandomizedSearchCV
5. **📈 Evaluation** - ประเมินผลด้วย MAE, RMSE, R² Score
6. ** Deployment** - Deploy เป็น web application ด้วย Streamlit Cloud
""")

# ช่องทางติดต่อ
st.subheader("📞 ช่องทางติดต่อ")
contact_cols = st.columns(3)

with contact_cols[0]:
    st.markdown(f"""
    <div class="info-box">
        <h4>📧 Email</h4>
        <p>{dev_email}</p>
    </div>
    """, unsafe_allow_html=True)

with contact_cols[1]:
    st.markdown(f"""
    <div class="info-box">
        <h4>💻 GitHub</h4>
        <p><a href="{dev_github}" target="_blank" style="color: #667eea;">{dev_github}</a></p>
    </div>
    """, unsafe_allow_html=True)

with contact_cols[2]:
    st.markdown("""
    <div class="info-box">
        <h4>📚 Dataset</h4>
        <p><a href="https://archive.ics.uci.edu/dataset/162/forest+fires" target="_blank" style="color: #667eea;">UCI Forest Fires</a></p>
    </div>
    """, unsafe_allow_html=True)

# References
st.markdown("---")
st.subheader("📚 References & Credits")
st.markdown("""
- **Dataset:** [UCI Forest Fires Dataset](https://archive.ics.uci.edu/dataset/162/forest+fires)
- **Paper:** Cortez, P. and Morais, A. (2007). "A Data Mining Approach to Predict Forest Fires using Meteorological Data"
- **Framework:** [Streamlit](https://streamlit.io/)
- **Libraries:** Scikit-Learn, XGBoost, Pandas, NumPy, Matplotlib, Seaborn
""")

# Copyright
st.markdown("---")
st.markdown(f"""
<div style="text-align: center; color: #888; font-size: 0.9em; padding: 1rem;">
    <p>© 2026 {dev_name}. All rights reserved.</p>
    <p>Developed with ❤️ using Streamlit</p>
</div>
""", unsafe_allow_html=True)