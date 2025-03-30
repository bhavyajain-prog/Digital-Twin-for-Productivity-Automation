# src/model_training/email_summarizer.py
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
import re

def summarize_email(email_body, num_sentences=3):
    """
    Generate a summary of an email by extracting the most important sentences
    
    Args:
        email_body: The body text of the email
        num_sentences: Number of sentences to include in summary
    
    Returns:
        A summary of the email
    """
    if not email_body or len(email_body) < 50:
        return email_body  # Return original if it's too short
    
    # Split into sentences
    sentences = re.split(r'(?<=[.!?])\s+', email_body)
    
    if len(sentences) <= num_sentences:
        return email_body  # Return original if it has fewer sentences than requested
    
    # Create TF-IDF features for sentences
    vectorizer = TfidfVectorizer(stop_words='english')
    tfidf_matrix = vectorizer.fit_transform(sentences)
    
    # Get sentence importance scores
    sentence_scores = np.sum(tfidf_matrix.toarray(), axis=1)
    
    # Get indices of top sentences
    top_indices = sentence_scores.argsort()[-num_sentences:]
    
    # Sort indices to maintain original order
    top_indices = sorted(top_indices)
    
    # Create summary
    summary = ' '.join([sentences[i] for i in top_indices])
    
    return summary