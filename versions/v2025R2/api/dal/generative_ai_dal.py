import os
import json
import requests
from dotenv import load_dotenv
from middleware.auth import get_sap_token

load_dotenv()

API_URL = os.getenv("SAP_GAI_API_URL")
RESOURCE_GROUP = "default"

system_prompt = """
Your Personal Training Assistant is here to help you with your fitness journey.
"""

def generate_text_from_sap(user_input: str, model="gpt-4o", extra_settings=None) -> str:
    if extra_settings is None:
        extra_settings = {}

    payload = {
        "model": model,
        "messages": [
            { "role": "system", "content": system_prompt },
            { "role": "user", "content": user_input }
        ],
        **extra_settings
    }

    access_token = get_sap_token()

    headers = {
        "Authorization": f"Bearer {access_token}",
        "Content-Type": "application/json",
        "AI-Resource-Group": RESOURCE_GROUP
    }

    response = requests.post(API_URL, headers=headers, json=payload)

    if response.status_code != 200:
        raise Exception(f"Failed to get AI response: {response.status_code} - {response.text}")

    print("🔹Prompt Used:", json.dumps(payload, indent=2))

    # Return just the message content
    return response.json()["choices"][0]["message"]["content"]
