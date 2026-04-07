import pandas as pd
from sklearn.tree import DecisionTreeClassifier

# Load dataset
data = pd.read_csv("disease_data.csv")

# Features and labels
X = data.drop("disease", axis=1)
y = data["disease"]

# Train model
model = DecisionTreeClassifier()
model.fit(X, y)

def predict_disease(symptoms):
    prediction = model.predict([symptoms])
    return prediction[0]