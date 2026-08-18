# ============================================
# 👨‍ ส่วนผู้พัฒนา (Developer Section)
# ============================================
st.markdown("---")
st.subheader("👨‍💻 ผู้พัฒนา (Developer)")

# ข้อมูลผู้พัฒนา - แก้ไขข้อมูลตามจริงของคุณ
developer_info = {
    "name": "นายพีรพัฒน์ กองบุตร",  # 👈 แก้ไขตรงนี้
    "role": "Data Scientist / ML Developer",
    "institution": "มหาวิทยาลัยราชภัฏนครปฐม",  # 👈 แก้ไขตรงนี้
    "project": "Wildfire Prediction System",
    "year": "2026",
    "description": """
    โปรเจคนี้พัฒนาขึ้นเพื่อทำนายพื้นที่ที่ถูกไฟป่าโดยใช้ Machine Learning 
    โดยอาศัยข้อมูลทางอุตุนิยมวิทยาและดัชนีความเสี่ยงไฟป่า (Fire Weather Index) 
    จาก UCI Forest Fires Dataset
    """
}

# แสดงข้อมูลผู้พัฒนา
col1, col2 = st.columns([1, 2])

with col1:
    # รูปโปรไฟล์ (ใช้ avatar หรือ emoji แทน)
    st.markdown("""
    <div style="text-align: center;">
        <div style="font-size: 80px;">👨‍💻</div>
        <h3 style="color: #FF6B35;">{name}</h3>
        <p style="color: #666; font-style: italic;">{role}</p>
        <p style="color: #888;">{institution}</p>
    </div>
    """.format(**developer_info), unsafe_allow_html=True)

with col2:
    st.markdown(f"""
    ### 📋 ข้อมูลโปรเจค
    - **ชื่อโปรเจค:** {developer_info['project']}
    - **ปีการศึกษา:** {developer_info['year']}
    - **ประเภท:** Machine Learning / Data Science
    - **Dataset:** UCI Forest Fires Dataset
    """)
    
    st.markdown(f"""
    ### 📖 คำอธิบาย
    {developer_info['description']}
    """)

# เทคโนโลยีที่ใช้
st.markdown("### 🛠️ เทคโนโลยีที่ใช้")

tech_cols = st.columns(4)

with tech_cols[0]:
    st.markdown("""
    **🐍 Programming**
    - Python 3.12
    - Pandas
    - NumPy
    """)

with tech_cols[1]:
    st.markdown("""
    **🤖 Machine Learning**
    - Scikit-Learn
    - XGBoost
    - Joblib
    """)

with tech_cols[2]:
    st.markdown("""
    **📊 Visualization**
    - Matplotlib
    - Seaborn
    """)

with tech_cols[3]:
    st.markdown("""
    **🌐 Web Framework**
    - Streamlit
    - Git & GitHub
    """)

# ช่องทางติดต่อ
st.markdown("### 📞 ช่องทางติดต่อ")

contact_cols = st.columns(3)

with contact_cols[0]:
    st.markdown("""
    **GitHub**
    - [github.com/yourusername](https://github.com/yourusername)
    """)

with contact_cols[1]:
    st.markdown("""
    **Email**
    - your.email@example.com
    """)

with contact_cols[2]:
    st.markdown("""
    **LinkedIn**
    - [linkedin.com/in/yourprofile](https://linkedin.com/in/yourprofile)
    """)

# Credit และ References
st.markdown("---")
st.subheader("📚 References & Credits")

st.markdown("""
- **Dataset:** [UCI Forest Fires Dataset](https://archive.ics.uci.edu/dataset/162/forest+fires)
- **Paper:** Cortez, P. and Morais, A. (2007). A Data Mining Approach to Predict Forest Fires using Meteorological Data.
- **Framework:** [Streamlit](https://streamlit.io/)
- **Libraries:** Scikit-Learn, XGBoost, Pandas, NumPy, Matplotlib, Seaborn
""")

# Copyright
st.markdown("---")
st.markdown(f"""
<div style="text-align: center; color: #888; font-size: 0.9em;">
    <p>© {developer_info['year']} {developer_info['name']}. All rights reserved.</p>
    <p>Developed with ❤️ using Streamlit</p>
</div>
""", unsafe_allow_html=True)