# src/model_training/email_classifier.py
import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
import pickle
import os

def train_email_classifier(email_df):
    """
    Train a model to classify emails into categories
    
    Args:
        email_df: DataFrame with email data
    
    Returns:
        trained model and vectorizer
    """
    if email_df.empty or len(email_df) < 5:
        print("Not enough email data to train the model yet.")
        return None, None
    
    # Prepare features and target
    X = email_df['full_text']
    y = email_df['category']
    
    # Split data into train and test sets
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42)
    
    # Create TF-IDF features
    vectorizer = TfidfVectorizer(max_features=1000)
    X_train_tfidf = vectorizer.fit_transform(X_train)
    X_test_tfidf = vectorizer.transform(X_test)
    
    # Train classifier
    classifier = RandomForestClassifier(n_estimators=100, random_state=42)
    classifier.fit(X_train_tfidf, y_train)
    
    # Evaluate
    accuracy = classifier.score(X_test_tfidf, y_test)
    print(f"Email classifier accuracy: {accuracy:.2f}")
    
    # Save the model
    os.makedirs("models", exist_ok=True)
    with open("models/email_classifier.pkl", "wb") as f:
        pickle.dump((classifier, vectorizer), f)
    
    return classifier, vectorizer

def classify_email(subject, body, classifier, vectorizer):
    """
    Classify a new email
    
    Args:
        subject: Email subject
        body: Email body
        classifier: Trained classifier
        vectorizer: Trained vectorizer
    
    Returns:
        Predicted category
    """
    if classifier is None or vectorizer is None:
        return "Unknown (Model not trained)"
    
    # Clean and combine text
    import re
    import string
    
    def clean_text(text):
        text = text.lower()
        text = re.sub(f'[{string.punctuation}]', ' ', text)
        text = re.sub(r'\s+', ' ', text).strip()
        return text
    
    clean_subject = clean_text(subject)
    clean_body = clean_text(body)
    full_text = clean_subject + " " + clean_body
    
    # Transform to TF-IDF features
    features = vectorizer.transform([full_text])
    
    # Predict
    category = classifier.predict(features)[0]
    
    return category