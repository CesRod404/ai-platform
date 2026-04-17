import os
import google.generativeai as genai

# Asegúrate de poner GEMINI_API_KEY en tu .env o variables de Render
api_key = os.getenv("GEMINI_API_KEY")
if api_key:
    genai.configure(api_key=api_key)

def create_embedding(text: str):
    result = genai.embed_content(
        model="models/text-embedding-004",
        content=text,
        task_type="retrieval_document"
    )
    return result['embedding']
