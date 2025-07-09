import os
from dotenv import load_dotenv
from middleware.auth import get_sap_token
from gen_ai_hub.proxy.native.openai import chat

RESOURCE_GROUP = "default"

system_prompt = """
Your Personal Training Assistant is here to help you with your fitness journey, keep it short and consice.
"""

def generate_text_from_sap(user_input: str, model="gpt-4o", extra_settings=None) -> str:
    if extra_settings is None:
        extra_settings = {}

    messages = [
        { "role": "system", "content": system_prompt },
        { "role": "user", "content": user_input }
    ]

    kwargs = dict(
        deployment_id='d9d3d64879df0b88',
        messages=messages,
        max_tokens=500,
        temperature=0.7,
        top_p=0.6,
        frequency_penalty=0.0,
        presence_penalty=0.0,
        stream=True,
    )

    stream = chat.completions.create(**kwargs)

    full_response = ""
    for chunk in stream:
        if not chunk.choices:
            continue
        delta = chunk.choices[0].delta
        print (chunk.choices[0].delta)
        if delta and isinstance(delta.content, str):
            full_response += delta.content
    return full_response
