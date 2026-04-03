# Secure API Request Script
# This script demonstrates:
# - Retrieving API key from environment variable
# - Sending authenticated API request
# - Handling different HTTP status codes
#
# Note:
# The API endpoint (api.example.com) is a placeholder.
# Connection error is expected and handled properly.

import os
import requests

api_key =os.getenv("API_KEY")

if not api_key:
    print("API key not found. please set the environment variable.")
    exit()
url ="https://api.example.com/data"

headers = {
    "Authorization": f"Bearer {api_key}"
}

try:
    # 4. Send GET request
    response = requests.get(url, headers=headers)

    # 5. Handle status codes
    if response.status_code == 200:
        print("Success:")
        print(response.json())

    elif response.status_code == 429:
        print("Rate limit reached. Try again later.")

    else:
        print("Request failed")
        print("Status Code:", response.status_code)

except requests.exceptions.RequestException as e:
    print("Error occurred while connecting to API.")
    print("This is expected if using a dummy URL.")
    print("Details:", e)