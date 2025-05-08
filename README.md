# 🛍️ Flipkart Reviews Sentiment Analysis and Rating Prediction

This project performs **Sentiment Analysis** and **Rating Prediction** on Flipkart product reviews using Natural Language Processing (NLP) and Machine Learning. It also includes a **Flask web app** where users can input reviews and receive sentiment predictions in real-time.

---

## 📌 Features

- Scrape product reviews from Flipkart using `scrap.py`.
- Clean and preprocess review data.
- Analyze sentiment (positive/negative) from review text.
- Predict star ratings from reviews using trained ML models.
- Deploy predictions via a Flask web application.

---

## 🗂️ Project Structure

```bash
.
├── scrap.py                      # Scrapes reviews from Flipkart
├── final_merged_flipkart_reviews.csv  # Consolidated dataset of reviews
├── flipkart_sentiment.ipynb     # Jupyter notebook for data analysis and model training
├── sentimental_model.pkl        # Trained ML model for sentiment prediction
├── vectorizer.pkl               # Text vectorizer (e.g., TF-IDF)
├── app.py                       # Flask web application
├── requirements.txt             # Required Python packages
└── README.md                    # Project documentation
```

---

## 🛠️ Installation

1. **Clone the repository**
```bash
git clone https://github.com/DhruvPatel1409/Flipkart-Reviews-Sentimental-Analysis-And-Prediction.git
cd Flipkart-Reviews-Sentimental-Analysis-And-Prediction
```

2. **Create and activate a virtual environment (optional but recommended)**
```bash
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

---

## 🚀 Running the Application

```bash
python app.py
```

Then open your browser and go to: [http://localhost:5000](http://localhost:5000)

---

## 📊 Model Training

You can retrain or explore the model training pipeline using the Jupyter notebook:

```bash
jupyter notebook flipkart_sentiment.ipynb
```

---

## 📉 Techniques Used

- Text Preprocessing (lowercasing, tokenization, stopword removal)
- TF-IDF Vectorization
- Logistic Regression / Random Forest for classification
- Flask for web deployment

---

## 🔍 Sample Prediction

| Input Review                                | Predicted Sentiment |
|---------------------------------------------|---------------------|
| "This product is amazing and fast!"         | Positive            |
| "Worst quality, very disappointed."         | Negative            |
| "The product is okay, works as expected."   | Neutral             |

