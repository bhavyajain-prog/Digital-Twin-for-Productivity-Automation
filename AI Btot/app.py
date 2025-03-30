# app.py
from flask import Flask, request, jsonify
import os
import sys
import pandas as pd



from src.inference.digital_twin import DigitalTwin
from src.data_collection.browsing_collector import save_browsing_data
from src.data_collection.email_collector import save_email_data
from src.preprocessing.browsing_preprocessor import load_browsing_data

app = Flask(__name__)
twin = DigitalTwin()

@app.route('/')
def home():
    return """
    <h1>Digital Twin API</h1>
    <p>Available endpoints:</p>
    <ul>
        <li>/add_browsing - Add browsing history data</li>
        <li>/analyze_browsing - Get user interest profile</li>
        <li>/process_email - Analyze and get suggestions for email</li>
    </ul>
    """

@app.route('/add_browsing', methods=['POST'])
def add_browsing():
    data = request.json
    
    if not data or 'url' not in data or 'timestamp' not in data or 'duration' not in data:
        return jsonify({'error': 'Missing required fields'}), 400
    
    record = save_browsing_data(data['url'], data['timestamp'], data['duration'])
    return jsonify({'status': 'success', 'record': record})

@app.route('/analyze_browsing', methods=['GET'])
def analyze_browsing():
    browsing_data = load_browsing_data()
    
    if browsing_data.empty:
        return jsonify({'status': 'No browsing data available'})
    
    profile = twin.analyze_browsing_history(browsing_data)
    return jsonify(profile)

@app.route('/process_email', methods=['POST'])
def process_email():
    data = request.json
    
    if not data or 'subject' not in data or 'body' not in data:
        return jsonify({'error': 'Missing required fields'}), 400
    
    # Optionally save the email if category is provided
    if 'category' in data:
        save_email_data(data['subject'], data['body'], data['category'])
    
    # Process the email
    result = twin.process_email(data['subject'], data['body'])
    return jsonify(result)

if __name__ == '__main__':
    print("Starting Digital Twin API...")
    app.run(debug=True, port=5000)