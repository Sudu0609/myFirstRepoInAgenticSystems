import json

# JSON formatted API response (string)
api_response = '''
{
    "id": "req_123",
    "status": "success",
    "result": {
        "text": "Hello world",
        "confidence": 0.98
    }
}
'''

# Parse JSON string into Python object
data = json.loads(api_response)

# Extract values
request_id = data["id"]
status = data["status"]
text_result = data["result"]["text"]
confidence_score = data["result"]["confidence"]

# Print extracted values
print("Request ID:", request_id)
print("Status:", status)
print("Text:", text_result)
print("Confidence:", confidence_score)

# Check confidence
if confidence_score < 0.9:
    print("Warning: Confidence score is below acceptable threshold!")

# Create follow-up result dictionary
follow_up_result = {
    "request_id": request_id,
    "processed": True,
    "message": "Result processed successfully"
}

# Convert dictionary to JSON
json_output = json.dumps(follow_up_result, indent=4)

# Write JSON output to file
with open("response.json", "w") as file:
    file.write(json_output)

print("JSON response saved to response.json")