import streamlit as st
import joblib
import pandas as pd

# Load trained model
model = joblib.load("model.pkl")

# -----------------------------
# PAGE CONFIG
# -----------------------------
st.set_page_config(
    page_title="Smart Student Performance Predictor",
    page_icon="🎓",
    layout="wide"
)

# -----------------------------
# CUSTOM CSS
# -----------------------------
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
}

.stButton > button:hover {
    transform: scale(1.03);
}

/* Sidebar */
section[data-testid="stSidebar"] {
    background-color: #111827;
}

</style>
""", unsafe_allow_html=True)

# -----------------------------
# HEADER
# -----------------------------
st.markdown("""
<h1>🎓 Smart Student Performance Predictor</h1>
<p style='text-align:center;font-size:18px;color:#cbd5e1'>
AI-Powered Academic Performance Analysis System
</p>
""", unsafe_allow_html=True)

# -----------------------------
# SDG 4 BANNER
# -----------------------------
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

# -----------------------------
# SIDEBAR INPUTS
# -----------------------------
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

# -----------------------------
# PREDICTION
# -----------------------------
if st.button("🚀 Predict Performance"):

    try:
        prediction = model.predict(
            [[attendance, study_hours, previous_marks]]
        )[0]

    except:
        # Fallback formula if model has issues
        prediction = (
            0.35 * attendance +
            0.25 * (study_hours * 8) +
            0.40 * previous_marks
        )

    # Smart Rule-Based Adjustments
    if attendance >= 95 and study_hours >= 10 and previous_marks >= 95:
        prediction = 100

    elif attendance <= 20 and study_hours <= 1 and previous_marks <= 20:
        prediction = 0

    # Restrict marks between 0 and 100
    prediction = float(prediction)
    prediction = max(0, min(100, prediction))
    prediction = round(prediction, 2)

    # -----------------------------
    # RESULT
    # -----------------------------
    st.subheader("📊 Prediction Result")

    col1, col2 = st.columns(2)

    with col1:
        st.metric(
            label="Predicted Final Marks",
            value=f"{prediction:.2f}"
        )

    with col2:

        if prediction < 40:
            status = "🔴 High Risk"
        elif prediction < 60:
            status = "🟡 Needs Improvement"
        elif prediction < 80:
            status = "🟢 Good Performance"
        else:
            status = "🏆 Excellent"

        st.metric(
            label="Performance Status",
            value=status
        )

    st.markdown("---")

    # -----------------------------
    # SCORE PROGRESS BAR
    # -----------------------------
    st.subheader("📈 Predicted Score")
    st.progress(int(prediction))

    # -----------------------------
    # AI SUGGESTIONS
    # -----------------------------
    st.subheader("🤖 AI Study Suggestions")

    if prediction < 40:

        st.error("⚠️ High Risk of Failure")

        st.write("""
        ✅ Increase study hours to 5–6 hours daily

        ✅ Improve attendance above 80%

        ✅ Focus on weak subjects

        ✅ Practice previous year papers

        ✅ Seek guidance from teachers
        """)

    elif prediction < 60:

        st.warning("📚 Needs Improvement")

        st.write("""
        ✅ Revise topics weekly

        ✅ Increase daily study time

        ✅ Improve attendance

        ✅ Take mock tests regularly
        """)

    elif prediction < 80:

        st.info("👍 Good Performance")

        st.write("""
        ✅ Continue regular study

        ✅ Solve more practice questions

        ✅ Improve consistency

        ✅ Maintain attendance
        """)

    else:

        st.success("🎉 Excellent Performance")

        st.write("""
        ✅ Maintain current study routine

        ✅ Continue regular revisions

        ✅ Practice advanced questions

        ✅ Help classmates and strengthen concepts
        """)

    # -----------------------------
    # INPUT ANALYSIS CHART
    # -----------------------------
    st.subheader("📊 Student Input Analysis")

    chart_data = pd.DataFrame(
        {
            "Value": [
                attendance,
                study_hours * 8.33,
                previous_marks
            ]
        },
        index=[
            "Attendance",
            "Study Hours",
            "Previous Marks"
        ]
    )

    st.bar_chart(chart_data)

# -----------------------------
# FOOTER
# -----------------------------
st.markdown("---")
st.markdown(
    "<center>Made with ❤️ by Malyadip Ghosh </center>",
    unsafe_allow_html=True
)