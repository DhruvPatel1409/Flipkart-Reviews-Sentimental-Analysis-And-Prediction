# 🛍️ Flipkart Reviews Sentiment Analysis and Rating Prediction

This project performs **Sentiment Analysis** and **Rating Prediction** on Flipkart product reviews using **Natural Language Processing (NLP)** and **Multinomial Naive Bayes**. It includes a **Streamlit web app** where users can input reviews and get real-time sentiment predictions (Positive, Negative, or Neutral).

---

## 📌 Features

- Scrape product reviews directly from Flipkart.
- Clean and preprocess raw review data for analysis.
- Analyze sentiment polarity (Positive / Negative / Neutral).
- Predict ratings using review text.
- Lightweight and interactive web app built using **Streamlit**.

---

## 🗂️ Project Structure

```bash
.
├── scrap.py                          # Script to scrape reviews from Flipkart
├── final_merged_flipkart_reviews.csv # Cleaned dataset of product reviews
├── flipkart_sentiment.ipynb         # Jupyter notebook for EDA, preprocessing, and training
├── sentimental_model.pkl            # Trained Multinomial Naive Bayes model
├── vectorizer.pkl                   # TF-IDF vectorizer
├── app.py                           # Streamlit web app
├── requirements.txt                 # List of dependencies
└── README.md                        # Project documentation
```

---

## 🛠️ Installation

1. **Clone the repository**
```bash
git clone https://github.com/DhruvPatel1409/Flipkart-Reviews-Sentimental-Analysis-And-Prediction.git
cd Flipkart-Reviews-Sentimental-Analysis-And-Prediction
```

2. **Create and activate a virtual environment (optional)**
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

---

## 🚀 Running the Web App (Streamlit)

To start the Streamlit application:

```bash
streamlit run app.py
```

Then open the browser window that pops up, or go to: [http://localhost:8501](http://localhost:8501)

---

## 📊 Model Training

The model was trained in `flipkart_sentiment.ipynb` using:

- **Multinomial Naive Bayes** (best suited for text classification problems)
- **TF-IDF Vectorization** for converting text to numerical format

To retrain the model, open the notebook:

```bash
jupyter notebook flipkart_sentiment.ipynb
```

---

## 📉 Techniques Used

- Data cleaning: Lowercasing, removing punctuation, stopword removal
- Tokenization and vectorization (TF-IDF)
- Sentiment classification: Positive, Negative, Neutral
- Model: Multinomial Naive Bayes
- Web framework: Streamlit

---

## 🔍 Sample Predictions

| Input Review                                | Predicted Sentiment |
|---------------------------------------------|---------------------|
| "This product is amazing and fast!"         | Positive            |
| "Worst quality, very disappointed."         | Negative            |
| "The product is okay, works as expected."   | Neutral             |
