```markdown
# 📧 Email Spam Classifier using Machine Learning (FastAPI)

This project is a simple **Email Spam Detection Web App** built using **FastAPI**, powered by a trained **Scikit-learn model** and **TF-IDF vectorizer**. The app predicts whether a given email text is spam or not.

---

## 🚀 Features

- Input email content through a web form
- Get instant predictions (Spam / Not Spam)
- Trained using TF-IDF vectorizer and Naive Bayes classifier
- Built with FastAPI and Jinja2 templating

---

## 🏗️ Project Structure

```

├── dataset/
│   └── mail\_data.csv
├── Model/
│   ├── spam\_classifier.pkl
│   └── tfidf\_vectorizer.pkl
├── templates/
│   └── index.html
├── main.py
├── requirements.txt
└── README.md

````

---

## 🔧 Requirements

Install the required Python packages:

```bash
pip install -r requirements.txt
````

---

## 🚦 How to Run

1. **Clone the repository**

```bash
git clone https://github.com/tirthosaha69/email-spam-classifier-using-ML.git
cd email-spam-classifier-using-ML
```

2. **Start the FastAPI server**

```bash
uvicorn main:app --reload
```

3. Open your browser and visit:
   [http://127.0.0.1:8000](http://127.0.0.1:8000)

---

## 📂 Dataset

* The dataset `mail_data.csv` is stored in the `dataset/` folder.
* It is preprocessed and used to train the spam classifier.

---

## 🧠 Model Info

* **Model**: Multinomial Naive Bayes
* **Vectorizer**: TF-IDF
* Saved in the `Model/` directory:

  * `spam_classifier.pkl`
  * `tfidf_vectorizer.pkl`

---

## 📸 UI Preview

The app provides a simple HTML form to enter email text and check predictions instantly.

---

## 🛠 Built With

* [FastAPI](https://fastapi.tiangolo.com/)
* [Scikit-learn](https://scikit-learn.org/)
* [Jinja2](https://jinja.palletsprojects.com/)
* [Pandas](https://pandas.pydata.org/)

---

## 📬 Contact

Feel free to connect with me on [GitHub](https://github.com/tirthosaha69) for collaboration or suggestions.

---

## ⭐ Give it a Star

If you found this useful, please ⭐ the repo to show support!

```


