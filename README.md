# 📧 Email Spam Classifier using Machine Learning (FastAPI)

This project is a **web-based email spam classifier** built using **FastAPI**. It allows users to enter an email message and get a real-time prediction on whether it is spam or not using a trained machine learning model.

---

## 🚀 Features

- Clean and simple UI using Jinja2 templates
- Spam/Ham prediction using a trained `MultinomialNB` model
- Fast and asynchronous backend with FastAPI
- Modular code structure (separate prediction logic)

---

## 🧠 ML Model Info

- Vectorizer: **TfidfVectorizer**
- Model: **Multinomial Naive Bayes (MultinomialNB)**
- Trained on a cleaned version of a labeled dataset (mail_data.csv)

---

## 🗂️ Project Structure

```

email-spam-classifier-using-ML/
│
├── main.py                  # FastAPI app entry point
├── utils.py                 # ML prediction logic
├── requirements.txt
├── templates/
│   └── index.html           # Web frontend
├── Model/
│   ├── spam\_classifier.pkl  # Trained ML model
│   └── tfidf\_vectorizer.pkl # TF-IDF vectorizer
├── dataset/
│   └── mail\_data.csv        # Raw dataset
└── README.md

````

---

## 🔧 Installation

```bash
git clone https://github.com/tirthosaha69/email-spam-classifier-using-ML.git
cd email-spam-classifier-using-ML
pip install -r requirements.txt
````

---

## ▶️ Run the App

```bash
uvicorn main:app --reload
```

Then open your browser and go to:
👉 **[http://127.0.0.1:8000/](http://127.0.0.1:8000/)**

---

## 🧪 Example

Enter a message like:
`Congratulations! You've won a free iPhone. Click here to claim.`
→ Prediction: **Spam Mail 🚫**

Or something like:
`Hey, are we still on for the meeting tomorrow?`
→ Prediction: **Ham Mail ✅**

---

## 📦 Requirements

See `requirements.txt`:

```txt
fastapi
uvicorn
scikit-learn
pandas
joblib
python-multipart
jinja2
```

---

## 🧑‍💻 Author

**Tirtho Saha**
📍 [GitHub](https://github.com/tirthosaha69)

---

## 📜 License

This project is licensed under the [MIT License](LICENSE).


