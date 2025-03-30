# src/inference/digital_twin.py
import os
import sys
import pickle
import pandas as pd

# Add the project root to the path to access other modules
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.preprocessing.browsing_preprocessor import preprocess_browsing_data
from src.feature_engineering.browsing_features import create_domain_frequency_features
from src.model_training.interest_model import get_interest_profile
from src.model_training.email_summarizer import summarize_email
from src.model_training.reply_generator import generate_reply
from src.model_training.email_classifier import classify_email

class DigitalTwin:
    def __init__(self):
        """Initialize the Digital Twin with pre-trained models if available"""
        self.interest_model = None
        self.interest_scaler = None
        self.email_classifier = None
        self.email_vectorizer = None
        
        # Load interest model if available
        try:
            with open("models/interest_model.pkl", "rb") as f:
                self.interest_model, self.interest_scaler = pickle.load(f)
            print("Interest model loaded successfully.")
        except FileNotFoundError:
            print("Interest model not found. Run training first.")
        
        # Load email classifier if available
        try:
            with open("models/email_classifier.pkl", "rb") as f:
                self.email_classifier, self.email_vectorizer = pickle.load(f)
            print("Email classifier loaded successfully.")
        except FileNotFoundError:
            print("Email classifier not found. Run training first.")
    
    def analyze_browsing_history(self, browsing_data):
        """
        Analyze browsing history and return user interest profile
        
        Args:
            browsing_data: DataFrame with browsing history
        
        Returns:
            User interest profile
        """
        if browsing_data.empty:
            return {"status": "No browsing data available"}
        
        # Preprocess data
        preprocessed_data = preprocess_browsing_data(browsing_data)
        
        # Create features
        domain_features = create_domain_frequency_features(preprocessed_data)
        
        # Generate interest profile
        if self.interest_model and not domain_features.empty:
            # Predict clusters for each domain
            features = domain_features[['visit_count', 'visit_percentage']]
            scaled_features = self.interest_scaler.transform(features)
            clusters = self.interest_model.predict(scaled_features)
            domain_features['interest_category'] = clusters
            
            # Get profile
            profile = get_interest_profile(domain_features, self.interest_model, self.interest_scaler)
            return profile
        else:
            return {"status": "Interest model not available or insufficient data"}
    
    def process_email(self, subject, body):
        """
        Process an email to classify, summarize, and generate a reply
        
        Args:
            subject: Email subject
            body: Email body
        
        Returns:
            Dictionary with email analysis results
        """
        result = {
            "original_length": len(body),
            "summary": None,
            "category": None,
            "suggested_reply": None
        }
        
        # Summarize email
        if len(body) > 100:  # Only summarize longer emails
            result["summary"] = summarize_email(body)
        else:
            result["summary"] = body
        
        # Classify email if model is available
        if self.email_classifier and self.email_vectorizer:
            result["category"] = classify_email(subject, body, self.email_classifier, self.email_vectorizer)
        else:
            result["category"] = "Unknown (Model not available)"
        
        # Generate reply
        result["suggested_reply"] = generate_reply(body, result["category"])
        
        return result