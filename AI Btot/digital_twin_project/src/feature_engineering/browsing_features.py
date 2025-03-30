# src/feature_engineering/browsing_features.py
import pandas as pd
import numpy as np

def create_domain_frequency_features(df):
    """Create features based on how often different domains are visited"""
    if df.empty:
        return pd.DataFrame()
    
    # Count visits per domain
    domain_counts = df['domain'].value_counts()
    
    # Convert to a DataFrame
    domain_features = pd.DataFrame({
        'domain': domain_counts.index,
        'visit_count': domain_counts.values
    })
    
    # Calculate percentage of total browsing time
    total_visits = domain_counts.sum()
    domain_features['visit_percentage'] = (domain_features['visit_count'] / total_visits * 100).round(2)
    
    return domain_features

def create_temporal_features(df):
    """Create features based on when browsing typically happens"""
    if df.empty:
        return pd.DataFrame()
    
    # Time of day distribution
    time_of_day_counts = df['time_of_day'].value_counts()
    time_features = pd.DataFrame({
        'time_of_day': time_of_day_counts.index,
        'visit_count': time_of_day_counts.values
    })
    
    # Day of week distribution
    day_mapping = {
        0: 'Monday', 1: 'Tuesday', 2: 'Wednesday',
        3: 'Thursday', 4: 'Friday', 5: 'Saturday', 6: 'Sunday'
    }
    df['day_name'] = df['day_of_week'].map(day_mapping)
    day_counts = df['day_name'].value_counts()
    day_features = pd.DataFrame({
        'day_of_week': day_counts.index,
        'visit_count': day_counts.values
    })
    
    return time_features, day_features