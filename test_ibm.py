import os
import requests
from dotenv import load_dotenv

load_dotenv()

# Get values from .env
API_KEY = os.getenv("WATSONX_API_KEY")
PROJECT_ID = os.getenv("WATSONX_PROJECT_ID")
MODEL_ID = os.getenv("WATSONX_MODEL_ID")
URL = os.getenv("WATSONX_URL")

# Step 1: Get IAM token
token_response = requests.post(
    "https://iam.cloud.ibm.com/identity/token",
    data={
        "apikey": API_KEY,
        "grant_type": "urn:ibm:params:oauth:grant-type:apikey"
    },
    headers={"Content-Type": "application/x-www-form-urlencoded"}
)

iam_token = token_response.json().get("access_token")
print("🔁 Raw Token Response:", token_response.status_code, token_response.text)

if not iam_token:
    print("❌ Failed to get token!")
    exit()

# Step 2: Make generation request
payload = {
    "model_id": MODEL_ID,
    "input": "What is a smart city?",
    "project_id": PROJECT_ID,  # ✅ REQUIRED!
    "parameters": {
        "decoding_method": "greedy",
        "max_new_tokens": 100
    }
}

headers = {
    "Authorization": f"Bearer {iam_token}",
    "Content-Type": "application/json"
}

response = requests.post(
    f"{URL}/ml/v1/text/generation?version=2023-05-29",
    headers=headers,
    json=payload
)

print(response.status_code)
print(response.text)
