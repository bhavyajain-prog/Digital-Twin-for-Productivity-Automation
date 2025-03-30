# src/model_training/reply_generator.py
import re

def detect_email_intent(email_body):
    """
    Detect the primary intent of an email
    
    Args:
        email_body: The body text of the email
    
    Returns:
        The detected intent (question, information, request, etc.)
    """
    # Convert to lowercase for case-insensitive matching
    text = email_body.lower()
    
    # Check for questions
    question_patterns = [
        r'\bwhat\b.*\?', r'\bhow\b.*\?', r'\bwhen\b.*\?', r'\bwhere\b.*\?',
        r'\bwhy\b.*\?', r'\bwho\b.*\?', r'\bcould you\b', r'\bcan you\b'
    ]
    for pattern in question_patterns:
        if re.search(pattern, text):
            return 'question'
    
    # Check for requests
    request_patterns = [
        r'\bplease\b', r'\brequest\b', r'\bcould you\b', r'\bcan you\b',
        r'\bneed\b.*\bto\b', r'\bwould like\b', r'\brecommend\b'
    ]
    for pattern in request_patterns:
        if re.search(pattern, text):
            return 'request'
    
    # Check for informational updates
    info_patterns = [
        r'\bjust wanted to\b', r'\bupdate\b', r'\binform\b', r'\blet you know\b',
        r'\bcompleted\b', r'\bfinished\b', r'\baccomplished\b'
    ]
    for pattern in info_patterns:
        if re.search(pattern, text):
            return 'information'
    
    # Check for gratitude
    gratitude_patterns = [
        r'\bthanks\b', r'\bthank you\b', r'\bappreciate\b', r'\bgrateful\b'
    ]
    for pattern in gratitude_patterns:
        if re.search(pattern, text):
            return 'gratitude'
    
    # Default to 'other' if no specific intent is detected
    return 'other'

def generate_reply(email_body, email_category):
    """
    Generate a smart reply based on email content and category
    
    Args:
        email_body: The body text of the email
        email_category: The category of the email (professional, personal, etc.)
    
    Returns:
        A suggested reply
    """
    # Detect the intent of the email
    intent = detect_email_intent(email_body)
    
    # Generate appropriate reply based on intent and category
    if email_category == 'professional':
        if intent == 'question':
            return "Thank you for your inquiry. I'll look into this matter and get back to you with the information as soon as possible."
        
        elif intent == 'request':
            return "Thank you for your request. I'll review the details and work on this. I'll update you on the progress shortly."
        
        elif intent == 'information':
            return "Thank you for sharing this information. I appreciate the update and will review the details."
        
        elif intent == 'gratitude':
            return "You're welcome. I'm glad I could be of assistance. Please let me know if you need anything else."
        
        else:
            return "Thank you for your email. I've received your message and will respond appropriately."
    
    elif email_category == 'personal':
        if intent == 'question':
            return "Hey there! Thanks for asking. Let me think about this and I'll get back to you soon!"
        
        elif intent == 'request':
            return "Hey! Thanks for reaching out. I'll see what I can do about your request."
        
        elif intent == 'information':
            return "Thanks for the update! I really appreciate you keeping me in the loop."
        
        elif intent == 'gratitude':
            return "No problem at all! Happy to help anytime."
        
        else:
            return "Hey! Thanks for your message. I'll get back to you soon."
    
    else:  # Default for other categories
        if intent == 'question':
            return "Thanks for your question. I'll respond when I have the information you need."
        
        elif intent == 'request':
            return "I've received your request and will take appropriate action."
        
        elif intent == 'information':
            return "Thank you for sharing this information with me."
        
        elif intent == 'gratitude':
            return "You're welcome. I'm glad I could help."
        
        else:
            return "Thank you for your message. I'll respond soon."