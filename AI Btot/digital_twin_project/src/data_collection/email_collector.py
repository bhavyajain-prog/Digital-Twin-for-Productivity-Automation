# src/data_collection/email_collector.py
import json
import os
import datetime

def save_email_data(subject, body, category):
    """
    Save an email to our dataset
    
    Args:
        subject (str): Email subject
        body (str): Email body
        category (str): Email category (professional, personal, etc.)
    """
    os.makedirs("data/emails", exist_ok=True)
    
    # Create a record
    record = {
        "subject": subject,
        "body": body,
        "category": category,
        "timestamp": datetime.datetime.now().isoformat()
    }
    
    # Save to file
    with open("data/emails/email_data.jsonl", "a") as f:
        f.write(json.dumps(record) + "\n")
    
    return record