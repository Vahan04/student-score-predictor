import os
import joblib
import pandas as pd

MODEL_PATH = os.path.join("model", "best_model.pkl")

def predict_score(hours_studied, sleep_hours, attendance_percent, previous_grade):
    model = joblib.load(MODEL_PATH)

    input_df = pd.DataFrame([{
        "hours_studied": hours_studied,
        "sleep_hours": sleep_hours,
        "attendance_percent": attendance_percent,
        "previous_grade": previous_grade
    }])

    pred = model.predict(input_df)[0]
    return round(pred, 2)

if __name__ == "__main__":
    # Example prediction
    score = predict_score(
        hours_studied=6,
        sleep_hours=7,
        attendance_percent=85,
        previous_grade=72
    )
    print(f"🎯 Predicted Final Score: {score}")