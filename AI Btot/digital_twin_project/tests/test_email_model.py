# tests/test_email_model.py
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.data_collection.email_collector import save_email_data
from src.preprocessing.email_preprocessor import load_email_data, preprocess_email_data
from src.model_training.email_classifier import train_email_classifier, classify_email

# Add some sample emails
print("Adding sample emails...")
save_email_data(
    "Meeting Tomorrow at 10AM",
    "Dear Team, Please join our project status meeting tomorrow at 10AM. Regards, Manager",
    "professional"
)

save_email_data(
    "Lunch this weekend?",
    "Hey! Do you want to grab lunch this weekend? It's been forever since we caught up!",
    "personal"
)

save_email_data(
    "Your Amazon Order #12345",
    "Thank you for your order. Your package will arrive on Tuesday. Click here to track your shipment.",
    "notification"
)

save_email_data(
    "Proposal for Project X",
    "Please find attached our proposal for Project X. We look forward to your feedback. Best regards, Business Team",
    "professional"
)

save_email_data(
    "Movie night!",
    "Are you free Friday night? We're planning to watch that new movie we talked about!",
    "personal"
)

# Load and preprocess data
print("\nLoading and preprocessing emails...")
email_data = load_email_data()
preprocessed_emails = preprocess_email_data(email_data)

# Train model
print("\nTraining email classifier...")
classifier, vectorizer = train_email_classifier(preprocessed_emails)

if classifier is not None:
    # Test with a new email
    print("\nTesting email classification with a new email...")
    test_subject = "Urgent: Project Deadline Changed"
    test_body = "Please note that the deadline for Project Y has been moved to next Friday. All deliverables must be completed by then."
    
    predicted_category = classify_email(test_subject, test_body, classifier, vectorizer)
    print(f"New email predicted category: {predicted_category}")
else:
    print("Model training failed. Make sure you have enough diverse email data.")