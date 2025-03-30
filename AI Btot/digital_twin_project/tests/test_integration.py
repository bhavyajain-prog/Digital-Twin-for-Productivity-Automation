# tests/test_integration.py
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.inference.digital_twin import DigitalTwin
from src.preprocessing.browsing_preprocessor import load_browsing_data

# Initialize Digital Twin
twin = DigitalTwin()

# Test browsing analysis
print("Testing browsing analysis...")
browsing_data = load_browsing_data()

if not browsing_data.empty:
    interest_profile = twin.analyze_browsing_history(browsing_data)
    print("\nUser Interest Profile:")
    for category, details in interest_profile.items():
        if category != "status":
            print(f"\n{category}:")
            print(f"  Top domains: {', '.join(details['top_domains'])}")
            print(f"  Percentage of browsing: {details['percentage_of_browsing']}%")
        else:
            print(f"Status: {details}")
else:
    print("No browsing data available. Run data collection tests first.")

# Test email processing
print("\nTesting email processing...")
test_email_subject = "Request for project status update"
test_email_body = """
Dear Team,

I hope this email finds you well. I'm writing to request an update on the current status of Project Alpha. 

Specifically, I would like to know:
1. What milestones have been completed so far?
2. Are there any issues or roadblocks currently impacting progress?
3. Do you anticipate meeting the planned delivery date of June 15th?

Please provide this information by the end of the week if possible. If you need more time, just let me know.

Thank you for your assistance.

Best regards,
Project Manager
"""

email_analysis = twin.process_email(test_email_subject, test_email_body)

print("\nEmail Analysis Results:")
print(f"Original length: {email_analysis['original_length']} characters")
print(f"Email category: {email_analysis['category']}")
print("\nSummary:")
print(email_analysis['summary'])
print("\nSuggested Reply:")
print(email_analysis['suggested_reply'])