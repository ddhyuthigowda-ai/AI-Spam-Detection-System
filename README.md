# 🛡️ AI Spam & Scam Detection System

An AI-powered hybrid spam detection engine that uses Machine Learning + rule-based keyword analysis to detect spam and scam messages in real time.

🌐 **Live Demo:** *(Add your Streamlit link here)*
📂 **Repository:** AI-Spam-Detection-System

---

## 🚀 Features

* ✅ Machine Learning–based spam classification (Logistic Regression)
* ✅ TF-IDF text vectorization
* ✅ Hybrid risk scoring (ML probability + suspicious keyword detection)
* ✅ Real-time spam probability meter (visual risk gauge)
* ✅ Live dashboard with message tracking
* ✅ English & Hindi language support
* ✅ Mobile-optimized UI
* ✅ Deployed on Streamlit Cloud

---

## 🧠 How It Works

1. User enters a message.
2. Text is converted into numerical features using TF-IDF.
3. A trained Logistic Regression model predicts spam probability.
4. A hybrid rule system checks suspicious keywords.
5. Final classification is shown with:

   * Spam probability
   * Risk level (Low / Medium / High)
   * Highlighted suspicious words
   * Live dashboard metrics

---

## 🛠️ Tech Stack

* Python
* Streamlit
* Scikit-learn
* Pandas
* TF-IDF Vectorizer
* Logistic Regression

---

## 📊 Model Training

* Dataset: SMS Spam Collection Dataset
* Preprocessing: Text cleaning + label encoding
* Algorithm: Logistic Regression
* Vectorization: TF-IDF
* Accuracy: ~97–99% (depending on split)

---

## 🎯 Use Cases

* SMS spam detection
* Scam message filtering
* Email filtering prototype
* Fraud risk analysis demo
* Educational ML project

---

## 📂 Project Structure

```id="readme-structure"
app.py                  # Streamlit UI
train_model.py          # Model training script
test_model.py           # CLI testing script
spam_model.pkl          # Trained model
vectorizer.pkl          # TF-IDF vectorizer
requirements.txt        # Dependencies
spam.csv                # Dataset
```

---

## 🏆 Hackathon Submission

This project demonstrates:

* End-to-end ML pipeline
* Model training & persistence
* Interactive web deployment
* Real-time risk scoring visualization
* Production-style app deployment

---

## 🔮 Future Improvements

* Deep Learning (LSTM/BERT)
* API integration
* Email integration
* Real-time SMS gateway support
* Database storage for analytics

---

# 👩‍💻 Author

**Dhyuthi Gowda**
AI & ML Enthusiast

---

# 📌 After Pasting

1. Replace:
   'https://ai-spam-detection-system-b3ygnkym9oxaheydwuenwu.streamlit.app/'
   with your actual live app URL.

2. Click **Commit changes**

