# src/preprocessing/browsing_preprocessor.py
import pandas as pd
import json
from datetime import datetime

def load_browsing_data():
    """Load browsing data from JSONL file into a pandas DataFrame"""
    records = []
    try:
        with open("data/browsing_history/browsing_data.jsonl", "r") as f:
            for line in f:
                records.append(json.loads(line))
        return pd.DataFrame(records)
    except FileNotFoundError:
        # Return empty DataFrame if no data yet
        return pd.DataFrame(columns=["url", "domain", "timestamp", "duration", "date", "time"])

def preprocess_browsing_data(df):
    """Clean and prepare browsing data for analysis"""
    if df.empty:
        return df
    
    # Convert timestamp to datetime
    df['datetime'] = pd.to_datetime(df['timestamp'])
    
    # Extract time features
    df['hour'] = df['datetime'].dt.hour
    df['day_of_week'] = df['datetime'].dt.dayofweek  # 0=Monday, 6=Sunday
    
    # Create time of day category
    def get_time_of_day(hour):
        if 5 <= hour < 12:
            return 'morning'
        elif 12 <= hour < 17:
            return 'afternoon'
        elif 17 <= hour < 22:
            return 'evening'
        else:
            return 'night'
    
    df['time_of_day'] = df['hour'].apply(get_time_of_day)
    
    return df