from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
import joblib

app = FastAPI()
templates = Jinja2Templates(directory="templates")

# Load model and vectorizer
model = joblib.load("Model/spam_classifier.pkl")
vectorizer = joblib.load("Model/tfidf_vectorizer.pkl")

@app.get("/", response_class=HTMLResponse)
async def home(request: Request):
    return templates.TemplateResponse("index.html", {"request": request, "result": None})

@app.post("/predict", response_class=HTMLResponse)
async def predict(request: Request, email_text: str = Form(...)):
    # Transform and predict
    vect_text = vectorizer.transform([email_text])
    prediction = model.predict(vect_text)[0]
    result = "Ham Mail ✅" if prediction == 1 else "Spam Mail 🚫"
    return templates.TemplateResponse("index.html", {"request": request, "result": result, "email_text": email_text})
