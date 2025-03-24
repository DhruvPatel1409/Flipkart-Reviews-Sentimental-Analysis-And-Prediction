import streamlit as st
import pickle
from sklearn.feature_extraction.text import TfidfVectorizer

# Load trained vectorizer and model
vectorizer = pickle.load(open("vectorizer.pkl", "rb"))
model = pickle.load(open("sentimental_model.pkl", "rb"))

def predict_sentiment(review):
    """Predict the sentiment of a given review."""
    transformed_review = vectorizer.transform([review])  # ✅ Wrap inside a list
    prediction = model.predict(transformed_review)
    
    if prediction[0] == 2:
        return "Positive 😊", "green"
    elif prediction[0] == 0:
        return "Negative 😡", "red"
    else:
        return "Neutral 😐", "orange"

# Streamlit UI
st.title("🛒 Flipkart Reviews Sentiment Analysis")
st.write("Enter a product review below to predict its sentiment.")

# User input
user_review = st.text_area("✍️ Enter your review:", "")

if st.button("🔍 Predict Sentiment"):
    if user_review.strip():
        sentiment, color = predict_sentiment(user_review)
        st.markdown(f"<h3 style='color:{color};'>📢 Predicted Sentiment: {sentiment}</h3>", unsafe_allow_html=True)
    else:
        st.warning("⚠️ Please enter a valid review.")
