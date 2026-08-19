import streamlit as st
import pandas as pd
import numpy as np
import joblib
import json
import os
import matplotlib.pyplot as plt

# ==========================================
# ⚙️ ส่วนตั้งค่า (แก้ไขข้อมูลตรงนี้)
# ==========================================
DEV_NAME = "สมชาย ใจดี"
DEV_ROLE = "นักศึกษา / Developer"
DEV_INSTITUTION = "มหาวิทยาลัย ABC"
DEV_GITHUB = "https://github.com/yourusername"
# ==========================================

st.set_page_config(page_title="Wildfire Prediction", page_icon="🔥", layout="wide")

st.title("🔥 Wildfire Prediction System")
st.markdown("---")

# --- Sidebar Input ---
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
    return pd.DataFrame({'X': [X], 'Y': [Y], 'month': [month], 'day': [day], 
                         'FFMC': [FFMC], 'DMC': [DMC], 'DC': [DC], 'ISI': [ISI], 
                         'temp': [temp], 'RH': [RH], 'wind': [wind], 'rain': [rain]})

input_df = user_input_features()
st.subheader("📋 Input Parameters")
st.write(input_df)

# --- Load Model ---
@st.cache_resource
def load_model():
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    model = joblib.load(os.path.join(BASE_DIR, 'best_model_joblib.pkl'))
    scaler = joblib.load(os.path.join(BASE_DIR, 'scaler.pkl'))
    features_path = os.path.join(BASE_DIR, 'features.json')
    features = json.load(open(features_path, 'r')) if os.path.exists(features_path) else None
    return model, scaler, features

# --- Real-time Prediction & Visualization (แก้ไขส่วนนี้) ---
try:
    model, scaler, features = load_model()
    
    # 1. คำนวณทำนายทันทีเมื่อ Input เปลี่ยน (ไม่ต้องกดปุ่ม)
    input_scaled = scaler.transform(input_df)
    prediction_log = model.predict(input_scaled)
    prediction = np.expm1(prediction_log[0])
    
    # 2. แสดงผล Metric ทันที
    st.subheader("🎯 Prediction Result")
    col1, col2, col3 = st.columns(3)
    
    with col1: 
        st.metric("Predicted Area (ha)", f"{prediction:.4f}")
    
    with col2:
        if prediction == 0: risk = "No Fire 🟢"
        elif prediction < 1: risk = "Low Risk 🟡"
        elif prediction < 10: risk = "Medium Risk 🟠"
        else: risk = "High Risk 🔴"
        st.metric("Risk Level", risk)
        
    with col3: 
        st.metric("Log(Area+1)", f"{prediction_log[0]:.4f}")
    
    # 3. วาดกราฟแบบ Real-time
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

# --- Developer Section ---
st.markdown("---")
st.subheader("👨‍💻 ผู้พัฒนา (Developer)")

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
image_path = os.path.join(BASE_DIR, 'images', 'developer.jpg')

st.markdown("""
<style>
    .dev-card { background: linear-gradient(135deg, #667eea 0%, #764ba2 100%); padding: 2rem; border-radius: 15px; color: white; margin: 1rem 0; }
    .info-box { background: #f8f9fa; padding: 1.5rem; border-radius: 10px; border-left: 4px solid #667eea; margin: 1rem 0; }
</style>
""", unsafe_allow_html=True)

col_img, col_info = st.columns([1, 3])
with col_img:
    if os.path.exists(image_path):
        st.image(image_path, caption=f"👤 {DEV_NAME}", width=200)
    else:
        st.markdown("<div style='font-size: 100px; text-align: center;'>👨‍💻</div>", unsafe_allow_html=True)

with col_info:
    st.markdown(f"""
    <div class="dev-card">
        <h2 style="margin: 0;">{DEV_NAME}</h2>
        <p style="margin: 0.5rem 0; font-size: 1.2rem; opacity: 0.9;">{DEV_ROLE}</p>
        <p style="margin: 0.3rem 0; opacity: 0.8;">🏫 {DEV_INSTITUTION}</p>
        <p style="margin: 0.3rem 0; opacity: 0.8;">📅 ปีการศึกษา 2026</p>
    </div>
    """, unsafe_allow_html=True)

st.markdown('<div class="info-box"><h4>🔥 Wildfire Prediction System</h4><p>โปรเจคนี้พัฒนาขึ้นเพื่อทำนายพื้นที่ที่ถูกไฟป่าโดยใช้ Machine Learning จาก UCI Forest Fires Dataset</p></div>', unsafe_allow_html=True)

st.subheader("🛠️ เทคโนโลยีที่ใช้")
tc = st.columns(4)
with tc[0]: st.markdown("**🐍 Programming**\n- Python\n- Pandas\n- NumPy")
with tc[1]: st.markdown("**🤖 ML**\n- Scikit-Learn\n- XGBoost\n- Joblib")
with tc[2]: st.markdown("**📊 Viz**\n- Matplotlib\n- Seaborn")
with tc[3]: st.markdown("** Web**\n- Streamlit\n- GitHub")

st.subheader("📞 ช่องทางติดต่อ")
st.markdown(f'<div class="info-box"><h4>💻 GitHub</h4><p><a href="{DEV_GITHUB}" target="_blank" style="color: #667eea;">{DEV_GITHUB}</a></p></div>', unsafe_allow_html=True)

st.markdown("---")
st.markdown(f'<div style="text-align: center; color: #888; font-size: 0.9em;"><p>© 2026 {DEV_NAME}. All rights reserved. | Developed with ❤️ using Streamlit</p></div>', unsafe_allow_html=True)