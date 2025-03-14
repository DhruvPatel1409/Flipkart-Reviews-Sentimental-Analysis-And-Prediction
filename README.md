# Flipkart-Reviews-Sentimental-Analysis-And-Prediction

📌 Project Overview
This project performs sentiment analysis on Flipkart product reviews using NLP and Machine Learning techniques. It classifies customer reviews as Positive, Negative, or Neutral and provides a sentiment confidence score.

The dataset contains customer reviews, overall ratings, and associated metadata. The primary goal is to gain insights into customer sentiments, improve product recommendations, and identify areas for improvement based on user feedback.

🚀 Features
✅ Data Cleaning & Preprocessing:

Removes URLs, special characters, emojis, and stopwords
Converts text to lowercase
Applies lemmatization for better text normalization
✅ Exploratory Data Analysis (EDA):

WordCloud visualization for frequent words
Sentiment distribution analysis using bar plots
Term Frequency-Inverse Document Frequency (TF-IDF) feature extraction
✅ Sentiment Classification:

Uses CardiffNLP’s Twitter RoBERTa model for sentiment prediction
Implements Machine Learning classifiers like Naïve Bayes, Random Forest, and XGBoost
Balances class distribution using SMOTE to avoid biases
✅ Model Training & Evaluation:

TfidfVectorizer converts text into numerical features
Multiple classifiers tested for best performance
Confusion matrix, accuracy, and classification reports used for evaluation
✅ Model Deployment:

The trained model is saved using pickle for reusability
Can be integrated into a web app or API for real-time predictions
