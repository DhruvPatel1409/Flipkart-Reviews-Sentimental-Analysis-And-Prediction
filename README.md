# Flipkart-Reviews-Sentimental-Analysis-And-Prediction

# 📖 Project Overview
### This project focuses on Sentiment Analysis on Flipkart product reviews using Natural Language Processing (NLP) 🧠 and Machine Learning 🤖 models. The goal is to classify reviews as Positive ✅, Negative ❌, or Neutral ⚖️, ensuring balanced class distribution for accurate sentiment prediction.

# 📂 Dataset
### The dataset used is final_merged_flipkart_reviews.csv, which contains customer reviews along with ratings. Data preprocessing is performed to clean the text and remove unwanted elements.

# ✨ Key Features
### ✅ Text Cleaning: Removes URLs, emojis, mentions, and special characters.
### 📝 Lemmatization: Converts words to their base form for consistency.
### 🔍 Sentiment Classification: Uses DistilBERT & Naïve Bayes Classifier.
### ⚖️ Class Balancing: SMOTE (Synthetic Minority Over-sampling Technique) was considered.
### 📊 TF-IDF Vectorization: Converts text into numerical representation.
### ☁️ WordCloud Visualization: Displays frequently used words in reviews.
### 📉 Sentiment Distribution Analysis: Visualized using Seaborn count plots.
# 🛠️ Technologies Used
### 🐍 Python
### 📚 NLP Libraries: NLTK, Transformers (DistilBERT)
### 📊 Data Processing: Pandas, NumPy, TextBlob
### 🎯 Machine Learning: Naïve Bayes, Random Forest, XGBoost, Gradient Boosting
### 📉 Class Imbalance Handling: SMOTE
### 🎨 Visualization: Seaborn, Matplotlib, WordCloud
# 📈 Model Training & Evaluation
## 1️⃣ Pipeline Approach:
### ✅ TF-IDF Vectorizer for text-to-numeric conversion.
### ✅ Multinomial Naïve Bayes (MNB) as the classifier.
## 2️⃣ Imbalanced Data Handling:
### 📉 Initially, reviews were unevenly distributed across sentiment categories.
### ⚖️ Preprocessing and balancing techniques improved distribution accuracy.
## 3️⃣ Performance Metrics:
### 📊 Accuracy Score
### 🔄 Confusion Matrix
# 💾 Saving and Loading the Model
### The trained model is serialized using Pickle (pickle.dump).
### It can be loaded later for real-time sentiment predictions.
