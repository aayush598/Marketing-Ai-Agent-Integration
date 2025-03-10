import requests
import json

# Define the API endpoint
API_URL = "http://127.0.0.1:5000/generate_campaign"

# Define the request payload with dummy values
payload = {
    "prompt": [
        "SmartFit Watch",
        ["Heart Rate Monitoring", "Step Tracking", "Sleep Analysis", "Bluetooth Connectivity"],
        "A next-gen smartwatch designed for fitness enthusiasts, offering advanced health tracking and seamless smartphone integration.",
        "Fitness enthusiasts, athletes, health-conscious individuals",
        "mail"
    ],
    "actions": ["scraped_images"]
}

# Send the POST request
response = requests.post(API_URL, json=payload)

# Print the response
if response.status_code == 200:
    print("Success! Here’s the response:")
    print(json.dumps(response.json(), indent=4))
else:
    print(f"Error {response.status_code}: {response.text}")
