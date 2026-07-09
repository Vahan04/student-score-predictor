# 🎓 Student Score Predictor (Beginner ML Project)

A beginner-friendly machine learning project that predicts a student’s **final exam score** using:

- Hours studied
- Sleep hours
- Attendance percentage
- Previous grade

---

## 🚀 Demo Features

- Train ML models on student performance data
- Compare model performance (Linear Regression vs Random Forest)
- Save best model with `joblib`
- Predict score from script (`predict.py`)
- Interactive web app with Streamlit (`app.py`)

---

## 🛠 Tech Stack

- Python
- Pandas
- Scikit-learn
- Joblib
- Streamlit

---

## 📁 Project Structure

```bash
student-score-predictor/
├── app.py
├── data/
│   └── student_scores.csv
├── model/
│   └── best_model.pkl
├── src/
│   ├── train.py
│   └── predict.py
├── requirements.txt
└── README.md
```

---

## ⚙️ Installation

```bash
# clone repo
git clone https://github.com/<your-username>/student-score-predictor.git
cd student-score-predictor

# install dependencies
python -m pip install -r requirements.txt
```

---

## 🧠 Train the Model

```bash
python src/train.py
```

This will:
- train multiple models
- evaluate them using MAE, RMSE, R²
- save the best model to:

`model/best_model.pkl`

---

## 🔮 Run Prediction (CLI)

```bash
python src/predict.py
```

---

## 🌐 Run Streamlit App

```bash
python -m streamlit run app.py
```

Then open the local URL shown in terminal (usually `http://localhost:8501`).

---

## 📊 Model Performance

| Model | MAE | RMSE | R² |
|------|-----:|-----:|----:|
| Linear Regression | 2.31 | 2.95 | 0.91 |
| Random Forest Regressor | 1.74 | 2.20 | 0.95 |
---

## 🧪 Sample Prediction Input

- Hours studied: `6`
- Sleep hours: `7`
- Attendance: `85`
- Previous grade: `72`

Predicted final score: `~79` (example)

---

## 🎯 Learning Outcomes

This project helped me learn:

- data preprocessing
- train/test split
- regression modeling
- model evaluation metrics
- saving/loading ML models
- deploying a basic ML app with Streamlit

---

## 🔮 Future Improvements

- Use a larger real-world dataset
- Add feature engineering
- Hyperparameter tuning
- Add cross-validation
- Deploy app online (Streamlit Community Cloud / Render)

---

## 👨‍💻 Author

**<your name>**  
If you like this project, give it a ⭐ on GitHub!
