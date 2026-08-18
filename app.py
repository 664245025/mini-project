# app.py - Wildfire Prediction System
# แก้ไขปัญหา NameError โดยย้าย import ไปด้านบนสุด

import streamlit as st
import pandas as pd
import numpy as np
import joblib
import json
import os
import matplotlib.pyplot as plt
import seaborn as sns

# Page config
st.set_page_config(
    page_title="Wildfire Prediction",
    page_icon="🔥",
    layout="wide"
)

# Title
st.title(" Wildfire Prediction System")
st.markdown("---")

# Sidebar for input
st.sidebar.header(" Input Parameters")

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

# Display input
st.subheader("📋 Input Parameters")
st.write(input_df)

# Load model with proper path handling
@st.cache_resource
def load_model():
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))
    
    model_path = os.path.join(BASE_DIR, 'best_model_joblib.pkl')
    scaler_path = os.path.join(BASE_DIR, 'scaler.pkl')
    features_path = os.path.join(BASE_DIR, 'features.json')
    
    # ตรวจสอบไฟล์
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

try:
    model, scaler, features = load_model()
    
    # Prediction
    st.subheader("🎯 Prediction Result")
    
    if st.button("🔮 Predict Burned Area", type="primary"):
        # Scale input
        input_scaled = scaler.transform(input_df)
        
        # Predict
        prediction_log = model.predict(input_scaled)
        prediction = np.expm1(prediction_log[0])  # inverse log
        
        # Display metrics
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
        
        # Visualization
        st.markdown("---")
        col1, col2 = st.columns(2)
        
        with col1:
            st.markdown("###  Predicted Area")
            # สร้างกราฟ - plt ถูก import แล้วด้านบนสุด
            fig, ax = plt.subplots(figsize=(6, 4))
            ax.bar(['Predicted Area'], [prediction], color='orange', edgecolor='black')
            ax.set_ylabel('Area (hectares)')
            ax.set_title('Predicted Burned Area')
            plt.tight_layout()
            st.pyplot(fig)
            plt.close(fig)  # ปิด figure เพื่อประหยัด memory
        
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
                plt.close(fig)  # ปิด figure

except FileNotFoundError as e:
    st.error(f"❌ {str(e)}")
    st.info("💡 กรุณาตรวจสอบว่าไฟล์โมเดลถูกอัพโหลดขึ้น GitHub แล้ว")
except Exception as e:
    st.error(f"❌ เกิดข้อผิดพลาด: {str(e)}")
    st.exception(e)  # แสดง traceback เต็มๆ

# Information
st.markdown("---")
st.subheader("ℹ️ About This System")
st.markdown("""
**Model:** Random Forest Regressor with Hyperparameter Tuning  
**Dataset:** UCI Forest Fires Dataset  
**Features Used:**
- Spatial coordinates (X, Y)
- Temporal features (month, day)
- Fire Weather Index (FFMC, DMC, DC, ISI)
- Meteorological data (temperature, humidity, wind, rain)
""")