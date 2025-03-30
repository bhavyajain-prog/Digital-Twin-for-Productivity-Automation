# tests/test_data_collection.py
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.data_collection.browsing_collector import save_browsing_data
import datetime

# Test with sample data
current_time = datetime.datetime.now().isoformat()
record = save_browsing_data(
    "https://www.example.com/page1",
    current_time,
    60  # seconds
)

print("Data collection test successful!")
print(f"Saved record: {record}")