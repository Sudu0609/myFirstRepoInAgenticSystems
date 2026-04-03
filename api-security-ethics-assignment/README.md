# Secure API Request Script

## Description
This project demonstrates secure and responsible API usage using Python.

## Features
- Uses environment variable to store API key
- Sends GET request with Authorization Bearer token
- Handles HTTP status codes (200, 429, others)
- Handles connection errors gracefully

## How to Run

1. Install dependencies:
   pip install requests

2. Set API key:
   setx API_KEY "your_api_key_here"

3. Run the script:
   python secure_api_request.py

## Note
The API endpoint used is a placeholder (https://api.example.com/data).
The connection error is expected and demonstrates proper error handling.