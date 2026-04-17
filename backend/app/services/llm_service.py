import os
import google.generativeai as genai
from app.services.memory_service import search_memory, store_memory

api_key = os.getenv("GEMINI_API_KEY")
if api_key:
    genai.configure(api_key=api_key)

# Usaremos la version ligera y ultra rapida flash
MODEL_NAME = "gemini-1.5-flash"

def ask_llm(db, message: str):
    memories = search_memory(db, message)
    context = "\n".join(memories)

    prompt = f"""
Contexto relevante de conversaciones pasadas:
{context}

Pregunta del usuario:
{message}
"""
    try:
        model = genai.GenerativeModel(MODEL_NAME)
        response = model.generate_content(prompt)
        answer = response.text
    except Exception as e:
        answer = f"Error conectando a Gemini API: {str(e)}"

    store_memory(db, message)
    store_memory(db, answer)

    return answer
