# utils.py

import joblib

# Load model and vectorizer
model = joblib.load("Model/spam_classifier.pkl")
vectorizer = joblib.load("Model/tfidf_vectorizer.pkl")

def predict_email(email_text: str) -> str:
    vect_text = vectorizer.transform([email_text])
    prediction = model.predict(vect_text)[0]
    return "Ham Mail ✅" if prediction == 1 else "Spam Mail 🚫"
