# tests/test_reply_generator.py
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.model_training.reply_generator import detect_email_intent, generate_reply

# Test emails with different intents
test_emails = [
    {
        "body": "Could you please review the attached proposal and provide your feedback by Friday?",
        "category": "professional",
        "expected_intent": "request"
    },
    {
        "body": "What time is our meeting scheduled for tomorrow?",
        "category": "professional",
        "expected_intent": "question"
    },
    {
        "body": "Just wanted to let you know that I completed the task you assigned. The files are in the shared folder.",
        "category": "professional",
        "expected_intent": "information"
    },
    {
        "body": "Hey! Are you free this weekend? We're planning to go hiking if you'd like to join!",
        "category": "personal",
        "expected_intent": "question"
    },
    {
        "body": "Thank you so much for your help with moving last weekend. I couldn't have done it without you!",
        "category": "personal",
        "expected_intent": "gratitude"
    }
]

print("Reply Generator Test")
print("-------------------")

for i, email in enumerate(test_emails, 1):
    print(f"\nTest {i}:")
    print(f"Email: \"{email['body']}\"")
    print(f"Category: {email['category']}")
    
    # Detect intent
    detected_intent = detect_email_intent(email['body'])
    print(f"Detected intent: {detected_intent}")
    print(f"Expected intent: {email['expected_intent']}")
    
    # Generate reply
    reply = generate_reply(email['body'], email['category'])
    print(f"Generated reply: \"{reply}\"")