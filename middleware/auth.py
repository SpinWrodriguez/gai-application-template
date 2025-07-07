import os
import json
import time
import requests
from pathlib import Path
from dotenv import load_dotenv

# Load .env file
load_dotenv()

TOKEN_URL = os.getenv("SAP_GAI_AUTH_URL")
CLIENT_ID = os.getenv("SAP_GAI_CLIENT_ID")
CLIENT_SECRET = os.getenv("SAP_GAI_CLIENT_SECRET")
TOKEN_PATH = Path(__file__).parent.parent / "sap_token.json"

def get_stored_token():
    if TOKEN_PATH.exists():
        with open(TOKEN_PATH, "r") as file:
            token_data = json.load(file)
            if time.time() < token_data.get("expires_in", 0):
                print("✅ Using cached SAP AI token")
                return token_data["access_token"]
    return None

def fetch_sap_token():
    try:
        headers = { "Content-Type": "application/x-www-form-urlencoded" }
        data = {
            "grant_type": "client_credentials",
            "client_id": CLIENT_ID,
            "client_secret": CLIENT_SECRET
        }
        response = requests.post(TOKEN_URL, data=data, headers=headers)
        response.raise_for_status()

        token_data = response.json()
        result = {
            "access_token": token_data["access_token"],
            "expires_in": time.time() + token_data["expires_in"]
        }

        with open(TOKEN_PATH, "w") as file:
            json.dump(result, file)

        print("📥 New SAP AI token retrieved")
        return result["access_token"]

    except requests.RequestException as e:
        print("❌ Error fetching SAP AI Core token:", e)
        raise

def get_sap_token():
    return get_stored_token() or fetch_sap_token()
