# tests/test_interest_model.py
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.preprocessing.browsing_preprocessor import load_browsing_data, preprocess_browsing_data
from src.feature_engineering.browsing_features import create_domain_frequency_features
from src.model_training.interest_model import train_interest_model, get_interest_profile

# Load and preprocess data
raw_data = load_browsing_data()
preprocessed_data = preprocess_browsing_data(raw_data)

# Create features and train model
if not preprocessed_data.empty:
    domain_features = create_domain_frequency_features(preprocessed_data)
    
    # Train the model
    kmeans, clusters, scaler = train_interest_model(domain_features, n_clusters=min(5, len(domain_features)))
    
    if kmeans is not None:
        # Get interest profile
        profile = get_interest_profile(domain_features, kmeans, scaler)
        
        print("Interest model test successful!")
        print("\nDomain clusters:")
        print(domain_features[['domain', 'visit_count', 'interest_category']].head(10))
        print("\nUser interest profile:")
        for category, details in profile.items():
            print(f"\n{category}:")
            print(f"  Top domains: {', '.join(details['top_domains'])}")
            print(f"  Percentage of browsing: {details['percentage_of_browsing']}%")
    else:
        print("Not enough data to train the model. Add more browsing data.")
else:
    print("No data found. Make sure to run the data collection test first.")