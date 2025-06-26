# app/services/granite_llm.py
import os
import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("WATSONX_API_KEY")
PROJECT_ID = os.getenv("WATSONX_PROJECT_ID")
MODEL_ID = os.getenv("WATSONX_MODEL_ID")
URL = os.getenv("WATSONX_URL")


def get_ibm_token():
    response = requests.post(
        "https://iam.cloud.ibm.com/identity/token",
        data={
            "apikey": API_KEY,
            "grant_type": "urn:ibm:params:oauth:grant-type:apikey"
        },
        headers={"Content-Type": "application/x-www-form-urlencoded"}
    )
    token_json = response.json()
    if "access_token" not in token_json:
        raise Exception("❌ IBM token error: " + str(token_json))
    return token_json["access_token"]


def ask_granite(prompt):
    access_token = get_ibm_token()

    payload = {
        "model_id": MODEL_ID,
        "input": prompt,
        "project_id": PROJECT_ID,  # 👈 Must be included
        "parameters": {
            "decoding_method": "greedy",
            "max_new_tokens": 200
        }
    }

    headers = {
        "Authorization": f"Bearer {access_token}",
        "Content-Type": "application/json"
    }

    response = requests.post(
        f"{URL}/ml/v1/text/generation?version=2023-05-29",
        headers=headers,
        json=payload
    )

    if response.status_code != 200:
        raise Exception(f"Error {response.status_code}: {response.text}")

    return response.json()["results"][0]["generated_text"]
