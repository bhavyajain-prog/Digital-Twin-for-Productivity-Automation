# tests/test_email_summarizer.py
import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from src.model_training.email_summarizer import summarize_email

# Test with a long email
test_email = """
Dear Team,

I hope this email finds you well. I wanted to update everyone on the progress of Project Alpha. As of yesterday, we have completed 75% of the development tasks according to our timeline. The frontend team has finished the UI components and is now working on integration with the backend APIs. The backend team has implemented all core functionalities and is now focusing on performance optimization and security enhancements.

We encountered a minor issue with the database migration last week, but the database team worked overtime to resolve it without impacting our delivery timeline. Special thanks to Jane and John for their exceptional work on this issue.

Our next milestone is scheduled for May 15th, when we plan to release the beta version for internal testing. Please make sure all your components are properly documented and tested before this date. 

The client has also requested a new feature for user activity tracking. We will discuss this in detail during our meeting tomorrow at 10AM. Please come prepared with your thoughts and potential implementation approaches.

Lastly, HR has announced that our annual team building event will take place on June 5th. Attendance is optional but encouraged. More details will be shared by the HR department next week.

If you have any questions or concerns, don't hesitate to reach out to me or your team lead.

Best regards,
Project Manager
"""

# Generate summary
summary = summarize_email(test_email, num_sentences=3)

print("Email Summarization Test")
print("------------------------")
print("\nOriginal Email:")
print(test_email)
print("\nSummarized Email (3 sentences):")
print(summary)