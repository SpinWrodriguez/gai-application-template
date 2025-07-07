from ..dal.generative_ai_dal import generate_text_from_sap

async def get_ai_response(prompt: str):
    return  generate_text_from_sap(prompt)
