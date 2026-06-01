import pandas as pd
from sklearn.linear_model import LinearRegression
import joblib

data = pd.read_csv("student_data.csv")

X = data[['attendance','study_hours','previous_marks']]
y = data['final_marks']

model = LinearRegression()
model.fit(X, y)

joblib.dump(model, "model.pkl")

print("Model saved successfully!")