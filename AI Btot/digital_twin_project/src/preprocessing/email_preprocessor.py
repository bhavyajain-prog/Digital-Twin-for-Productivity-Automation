# src/preprocessing/email_preprocessor.py
import pandas as pd
import json
import re
import string

def load_email_data():
    """Load email data from JSONL file into a pandas DataFrame"""
    records = []
    try:
        with open("data/emails/email_data.jsonl", "r") as f:
            for line in f:
                records.append(json.loads(line))
        return pd.DataFrame(records)
    except FileNotFoundError:
        # Return empty DataFrame if no data yet
        return pd.DataFrame(columns=["subject", "body", "category", "timestamp"])

def preprocess_email_data(df):
    """Clean and prepare email data for analysis"""
    if df.empty:
        return df
    
    # Clean text
    def clean_text(text):
        # Convert to lowercase
        text = text.lower()
        # Remove punctuation
        text = re.sub(f'[{string.punctuation}]', ' ', text)
        # Remove extra whitespace
        text = re.sub(r'\s+', ' ', text).strip()
        return text
    
    df['clean_subject'] = df['subject'].apply(clean_text)
    df['clean_body'] = df['body'].apply(clean_text)
    
    # Combine subject and body for analysis
    df['full_text'] = df['clean_subject'] + " " + df['clean_body']
    
    return df