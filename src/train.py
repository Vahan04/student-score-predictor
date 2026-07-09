import os
import joblib
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score
from sklearn.linear_model import LinearRegression
from sklearn.ensemble import RandomForestRegressor

# Paths
DATA_PATH = os.path.join("student_score", "data", "student_scores.csv")
MODEL_DIR = "model"
MODEL_PATH = os.path.join(MODEL_DIR, "best_model.pkl")

# 1. Load data
df = pd.read_csv(DATA_PATH)

# 2. Features/target
X = df[["hours_studied", "sleep_hours", "attendance_percent", "previous_grade"]]
y = df["final_score"]

# 3. Split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# 4. Train models
models = {
    "LinearRegression": LinearRegression(),
    "RandomForest": RandomForestRegressor(n_estimators=200, random_state=42)
}

best_model = None
best_r2 = float("-inf")

print("Model Evaluation Results:")
for name, model in models.items():
    model.fit(X_train, y_train)
    preds = model.predict(X_test)

    mae = mean_absolute_error(y_test, preds)
    rmse = mean_squared_error(y_test, preds, squared=False)
    r2 = r2_score(y_test, preds)

    print(f"\n{name}")
    print(f"MAE : {mae:.3f}")
    print(f"RMSE: {rmse:.3f}")
    print(f"R2  : {r2:.3f}")

    if r2 > best_r2:
        best_r2 = r2
        best_model = model

# 5. Save best model
os.makedirs(MODEL_DIR, exist_ok=True)
joblib.dump(best_model, MODEL_PATH)
print(f"\n✅ Best model saved to: {MODEL_PATH}")