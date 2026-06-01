import streamlit as st
import joblib
import pandas as pd

# Load trained model
model = joblib.load("model.pkl")

# Page Configuration
st.set_page_config(
    page_title="Smart Student Performance Predictor",
    page_icon="🎓",
    layout="wide"
)

# Custom CSS
st.markdown("""
<style>

/* Main Background */
.stApp {
    background: linear-gradient(135deg, #0f172a, #1e293b);
    color: white;
}

/* Title */
h1 {
    text-align: center;
    color: #38bdf8 !important;
    font-weight: bold;
}

/* Metric Card */
div[data-testid="stMetric"] {
    background-color: #1e293b;
    padding: 15px;
    border-radius: 15px;
    border: 1px solid #38bdf8;
    box-shadow: 0 0 15px rgba(56,189,248,0.3);
}

/* Buttons */
.stButton > button {
    background: linear-gradient(90deg,#2563eb,#06b6d4);
    color: white;
    border-radius: 10px;
    border: none;
    font-weight: bold;
    width: 100%;
    height: 50px;
    transition: 0.3s;
}

.stButton > button:hover {
    transform: scale(1.03);
    box-shadow: 0 0 15px #38bdf8;
}

/* Sidebar */
section[data-testid="stSidebar"] {
    background-color: #111827;
}

</style>
""", unsafe_allow_html=True)

# Header
st.markdown("""
<h1>🎓 Smart Student Performance Predictor</h1>
<p style='text-align:center;font-size:18px;color:#cbd5e1'>
AI-Powered Academic Performance Analysis System
</p>
""", unsafe_allow_html=True)

# SDG Banner
st.markdown("""
<div style="
background: linear-gradient(90deg,#2563eb,#06b6d4);
padding:20px;
border-radius:15px;
text-align:center;
margin-bottom:25px;
">
<h2>📚 SDG 4 - Quality Education</h2>
<p>
Helping students improve learning outcomes through Machine Learning.
</p>
</div>
""", unsafe_allow_html=True)

# Sidebar Inputs
st.sidebar.header("📥 Student Details")

attendance = st.sidebar.slider(
    "Attendance (%)",
    0,
    100,
    75
)

study_hours = st.sidebar.slider(
    "Study Hours Per Day",
    0,
    12,
    4
)

previous_marks = st.sidebar.slider(
    "Previous Marks",
    0,
    100,
    60
)

# Prediction Button
if st.button("🚀 Predict Performance"):

    prediction = model.predict(
        [[attendance, study_hours, previous_marks]]
    )[0]

    st.subheader("📊 Prediction Result")

    col1, col2 = st.columns(2)

    with col1:
        st.metric(
            label="Predicted Final Marks",
            value=f"{prediction:.2f}"
        )

    with col2:

        if prediction < 40:
            status = "High Risk"
        elif prediction < 60:
            status = "Needs Improvement"
        else:
            status = "Good Performance"

        st.metric(
            label="Performance Status",
            value=status
        )

    st.markdown("---")

    # Suggestions
    st.subheader("🤖 AI Study Suggestions")

    if prediction < 40:

        st.error("⚠️ High Risk of Failure")

        st.write("""
        - Increase study hours to 5–6 hours daily
        - Improve attendance above 80%
        - Focus on weak subjects
        - Practice previous year questions
        - Seek guidance from teachers
        """)

    elif prediction < 60:

        st.warning("📚 Needs Improvement")

        st.write("""
        - Revise topics weekly
        - Increase daily study time
        - Improve attendance
        - Take mock tests regularly
        """)

    else:

        st.success("🎉 Likely to Perform Well")

        st.write("""
        - Maintain current study routine
        - Continue regular revisions
        - Practice advanced questions
        - Help peers and strengthen concepts
        """)

    # Input Summary Chart
    st.subheader("📈 Student Input Analysis")

    chart_data = pd.DataFrame({
        "Value": [
            attendance,
            study_hours,
            previous_marks
        ]
    },
    index=[
        "Attendance",
        "Study Hours",
        "Previous Marks"
    ])

    st.bar_chart(chart_data)

# Footer
st.markdown("---")
st.markdown(
    "<center>Made with ❤️ using Streamlit & Machine Learning</center>",
    unsafe_allow_html=True
)