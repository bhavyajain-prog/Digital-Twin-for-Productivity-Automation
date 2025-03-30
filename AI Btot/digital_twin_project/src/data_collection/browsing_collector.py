# src/data_collection/browsing_collector.py
import json
import datetime
import os

def save_browsing_data(url, timestamp, duration):
    """
    Save a browsing history entry to our dataset
    
    Args:
        url (str): The URL visited
        timestamp (str): When the URL was visited (ISO format)
        duration (int): Time spent in seconds
    """
    # Create data directory if it doesn't exist
    os.makedirs("data/browsing_history", exist_ok=True)
    
    # Extract domain from URL
    domain = url.split("//")[-1].split("/")[0]
    
    # Create a record
    record = {
        "url": url,
        "domain": domain,
        "timestamp": timestamp,
        "duration": duration,
        "date": timestamp.split("T")[0],
        "time": timestamp.split("T")[1].split(".")[0]
    }
    
    # Save to file
    with open("data/browsing_history/browsing_data.jsonl", "a") as f:
        f.write(json.dumps(record) + "\n")
    
    return record