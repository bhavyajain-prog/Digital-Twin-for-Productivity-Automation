# tests/test_feature_engineering.py
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.preprocessing.browsing_preprocessor import load_browsing_data, preprocess_browsing_data
from src.feature_engineering.browsing_features import create_domain_frequency_features, create_temporal_features

# Load and preprocess data
raw_data = load_browsing_data()
preprocessed_data = preprocess_browsing_data(raw_data)

# Generate features
if not preprocessed_data.empty:
    domain_features = create_domain_frequency_features(preprocessed_data)
    time_features, day_features = create_temporal_features(preprocessed_data)
    
    print("Feature engineering test successful!")
    print("\nDomain frequency features:")
    print(domain_features.head())
    print("\nTime of day features:")
    print(time_features)
    print("\nDay of week features:")
    print(day_features)
else:
    print("No data found. Make sure to run the data collection test first.")