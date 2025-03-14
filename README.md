# Flipkart-Reviews-Sentimental-Analysis-And-Prediction

# Project Overview
### This project focuses on performing Sentiment Analysis on Flipkart product reviews using Natural Language Processing (NLP) techniques and Machine Learning models. The goal is to classify reviews as Positive, Negative, or Neutral, ensuring balanced class distribution for accurate sentiment prediction.

# Dataset
### The dataset used is final_merged_flipkart_reviews.csv, which contains customer reviews along with ratings. Data preprocessing is performed to clean the text and remove unwanted elements.

# Key Features
### Text Cleaning: Removal of URLs, emojis, mentions, and special characters.
### Lemmatization: Used to standardize words to their base form.
### Sentiment Classification: Implemented using DistilBERT and Naïve Bayes Classifier.
### Class Balancing: SMOTE (Synthetic Minority Over-sampling Technique) was considered but not always used.
### TF-IDF Vectorization: Converts text data into numerical form for model training.
### WordCloud Visualization: Displays frequently used words in reviews.
### Sentiment Distribution Analysis: Visualized using Seaborn count plots.
# Technologies Used
### Python
### NLP Libraries: NLTK, Transformers (DistilBERT)
### Data Processing: Pandas, NumPy, TextBlob
### Machine Learning: Naïve Bayes, Random Forest, XGBoost, Gradient Boosting
### Class Imbalance Handling: SMOTE
### Visualization: Seaborn, Matplotlib, WordCloud
# Model Training & Evaluation
## Pipeline Approach:
### Implemented a TF-IDF Vectorizer to convert text into numerical form.
### Used Multinomial Naïve Bayes (MNB) as a classifier.
## Imbalanced Data Handling:
### Initially, reviews were unevenly distributed across sentiment categories.
### After fine-tuning preprocessing and balancing strategies, a more accurate distribution was achieved.
## Performance Metrics:
### Accuracy Score
### Confusion Matrix
# Saving and Loading the Model
### The trained model is serialized using Pickle (pickle.dump).
### It can be loaded later for real-time sentiment predictions.
