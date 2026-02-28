import pickle

# Load model and vectorizer
model = pickle.load(open("spam_model.pkl", "rb"))
vectorizer = pickle.load(open("vectorizer.pkl", "rb"))

while True:
    message = input("Enter a message: ")
    data = vectorizer.transform([message])
    prediction = model.predict(data)

    if prediction[0] == 1:
        print("⚠️ Spam detected!")
    else:
        print("✅ Not Spam")