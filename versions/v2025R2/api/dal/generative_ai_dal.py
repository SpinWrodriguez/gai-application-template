import os
from dotenv import load_dotenv
from middleware.auth import get_sap_token
from gen_ai_hub.proxy.native.openai import chat

RESOURCE_GROUP = "default"

system_prompt = """
Your Personal Training Assistant is here to help you with your fitness journey.
"""

def generate_text_from_sap(user_input: str, model="gpt-4o", extra_settings=None) -> str:
    if extra_settings is None:
        extra_settings = {}

    messages = [
        {  "role": "system", "content": system_prompt},
        {  "role": "user", "content": user_input }
    ]

    kwargs = dict(deployment_id='d9d3d64879df0b88', messages=messages)
    response = chat.completions.create(**kwargs)
    return (response.choices[0].message.content)