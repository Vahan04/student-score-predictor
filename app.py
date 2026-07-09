import joblib
import pandas as pd
import streamlit as st

st.set_page_config(page_title="Student Score Predictor", page_icon="🎓")

st.title("🎓 Student Score Predictor")
st.write("Predict final exam score using study/sleep/attendance/previous grade.")

model = joblib.load("model/best_model.pkl")

hours_studied = st.slider("Hours Studied", 0, 12, 5)
sleep_hours = st.slider("Sleep Hours", 0, 12, 7)
attendance_percent = st.slider("Attendance %", 0, 100, 80)
previous_grade = st.slider("Previous Grade", 0, 100, 70)

if st.button("Predict Score"):
    input_df = pd.DataFrame([{
        "hours_studied": hours_studied,
        "sleep_hours": sleep_hours,
        "attendance_percent": attendance_percent,
        "previous_grade": previous_grade
    }])
    pred = min(100, max(0, model.predict(input_df)[0]))
    st.success(f"Predicted Final Score: {pred:.2f}")