# ============================================
# 👨💻 ส่วนผู้พัฒนา (Developer Section) พร้อมรูป
# ============================================
st.markdown("---")
st.subheader("👨💻 ผู้พัฒนา (Developer)")

# ️ แก้ไขข้อมูลส่วนตัวตรงนี้
dev_name = "นายพีรพัฒน์ กองงบุตร"
dev_role = "Data Scientist / ML Developer"
dev_institution = "มหาวิทยาลัยราชภัฏนครปฐม"
dev_email = "your.email@example.com"
dev_github = "https://github.com/yourusername"

# โหลดรูปผู้พัฒนา
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
image_path = os.path.join(BASE_DIR, 'images',' mark.jpg')

# ตรวจสอบว่ามีรูปหรือไม่
if os.path.exists(image_path):
    developer_image = image_path
else:
    developer_image = None  # ใช้ emoji แทนถ้าไม่มีรูป

# Custom CSS สำหรับ styling
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
    .developer-image-container {
        text-align: center;
    }
    .developer-image {
        width: 180px;
        height: 180px;
        border-radius: 50%;
        border: 5px solid white;
        box-shadow: 0 4px 15px rgba(0,0,0,0.3);
        object-fit: cover;
    }
    .developer-emoji {
        font-size: 120px;
        text-align: center;
        margin: 10px 0;
    }
    .developer-info {
        padding: 1rem 0;
    }
    .developer-name {
        font-size: 2rem;
        font-weight: bold;
        margin-bottom: 0.5rem;
    }
    .developer-role {
        font-size: 1.2rem;
        opacity: 0.9;
        margin-bottom: 0.5rem;
    }
    .developer-detail {
        font-size: 1rem;
        opacity: 0.8;
        margin: 0.3rem 0;
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
if developer_image:
    # มีรูปจริง - แสดงรูป + ข้อมูล
    st.markdown(f"""
    <div class="developer-card">
        <div style="display: flex; align-items: center; gap: 2rem; flex-wrap: wrap;">
            <div class="developer-image-container">
                <img src="data:image/jpeg;base64," class="developer-image" 
                     onerror="this.style.display='none'; this.nextElementSibling.style.display='block';">
                <div class="developer-emoji" style="display: none;">👨‍</div>
            </div>
            <div class="developer-info" style="flex: 1;">
                <div class="developer-name">{dev_name}</div>
                <div class="developer-role">{dev_role}</div>
                <div class="developer-detail">🏫 {dev_institution}</div>
                <div class="developer-detail">📅 ปีการศึกษา 2026</div>
                <div class="developer-detail"> {dev_email}</div>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    # แสดงรูปด้วย st.image (วิธีที่ง่ายกว่าและ reliable กว่า)
    col_img, col_info = st.columns([1, 2])
    
    with col_img:
        st.image(
            developer_image,
            caption=f"👤 {dev_name}",
            width=200,
            use_column_width=False
        )
    
    with col_info:
        st.markdown(f"""
        ### 👤 ข้อมูลผู้พัฒนา
        - **ชื่อ:** {dev_name}
        - **บทบาท:** {dev_role}
        - **สถาบัน:** {dev_institution}
        - **อีเมล:** {dev_email}
        - **GitHub:** [{dev_github}]({dev_github})
        """)
else:
    # ไม่มีรูป - ใช้ emoji แทน
    st.markdown(f"""
    <div class="developer-card">
        <div style="display: flex; align-items: center; gap: 2rem; flex-wrap: wrap;">
            <div class="developer-emoji">‍💻</div>
            <div class="developer-info" style="flex: 1;">
                <div class="developer-name">{dev_name}</div>
                <div class="developer-role">{dev_role}</div>
                <div class="developer-detail">🏫 {dev_institution}</div>
                <div class="developer-detail">📅 ปีการศึกษา 2026</div>
                <div class="developer-detail">📧 {dev_email}</div>
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)
    
    st.info("💡 **คำแนะนำ:** อัพโหลดรูปผู้พัฒนาไปที่โฟลเดอร์ `images/developer.jpg` ใน GitHub repo เพื่อแสดงรูปจริง")

# ข้อมูลโปรเจค
st.markdown("""
<div class="info-box">
    <h4>🔥 Wildfire Prediction System</h4>
    <p>โปรเจคนี้พัฒนาขึ้นเพื่อทำนายพื้นที่ที่ถูกไฟป่าโดยใช้ Machine Learning 
    โดยอาศัยข้อมูลทางอุตุนิยมวิทยาและดัชนีความเสี่ยงไฟป่า (Fire Weather Index) 
    จาก UCI Forest Fires Dataset</p>
    <p><strong>วัตถุประสงค์:</strong> เพื่อสร้างโมเดลที่สามารถทำนายพื้นที่ที่ถูกไฟป่าได้อย่างแม่นยำ 
    และช่วยในการวางแผนป้องกันและจัดการไฟป่า</p>
</div>
""", unsafe_allow_html=True)

# เทคโนโลยีที่ใช้
st.subheader("️ เทคโนโลยีและเครื่องมือที่ใช้")

tech_categories = {
    "🐍 Programming Languages": ["Python 3.12"],
    "📊 Data Processing": ["Pandas", "NumPy"],
    "🤖 Machine Learning": ["Scikit-Learn", "XGBoost", "Joblib"],
    "📈 Visualization": ["Matplotlib", "Seaborn"],
    "🌐 Web Framework": ["Streamlit"],
    "🔧 Version Control": ["Git", "GitHub"],
    "☁️ Deployment": ["Streamlit Cloud"]
}

for category, techs in tech_categories.items():
    tech_badges = " ".join([f'<span class="tech-badge">{tech}</span>' for tech in techs])
    st.markdown(f"**{category}** {tech_badges}")
    st.markdown("")

# ขั้นตอนการพัฒนา
st.subheader("📝 ขั้นตอนการพัฒนา")

st.markdown("""
1. **📊 Data Collection** - รวบรวม dataset จาก UCI Machine Learning Repository
2. **🧹 Data Preprocessing** - ทำความสะอาดข้อมูล, แปลง categorical variables, log transform
3. **🤖 Model Development** - สร้างและเปรียบเทียบหลาย ML algorithms (SVM, Random Forest, XGBoost)
4. **🎯 Hyperparameter Tuning** - ปรับแต่งพารามิเตอร์ด้วย RandomizedSearchCV
5. **📈 Evaluation** - ประเมินผลด้วย MAE, RMSE, R² Score
6. **🌐 Deployment** - Deploy เป็น web application ด้วย Streamlit Cloud
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

# Copyright Footer
st.markdown("---")
st.markdown(f"""
<div style="text-align: center; color: #888; font-size: 0.9em; padding: 1rem;">
    <p>© 2026 {dev_name}. All rights reserved.</p>
    <p>Developed with ❤️ using <a href="https://streamlit.io/" style="color: #FF6B35;">Streamlit</a></p>
</div>
""", unsafe_allow_html=True)