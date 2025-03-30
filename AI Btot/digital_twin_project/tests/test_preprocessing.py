# tests/test_preprocessing.py
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.preprocessing.browsing_preprocessor import load_browsing_data, preprocess_browsing_data

# Load and preprocess data
raw_data = load_browsing_data()
preprocessed_data = preprocess_browsing_data(raw_data)

# Show sample of preprocessed data
print("Preprocessing test successful!")
if not preprocessed_data.empty:
    print(preprocessed_data.head())
else:
    print("No data found. Make sure to run the data collection test first.")