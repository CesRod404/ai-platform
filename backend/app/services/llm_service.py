import requests

from app.services.memory_service import search_memory, store_memory

OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL_NAME = "qwen2.5-coder:7b"


def ask_llm(db, message: str):

    memories = search_memory(db, message)

    context = "\n".join(memories)

    prompt = f"""
Contexto relevante de conversaciones pasadas:
{context}

Pregunta del usuario:
{message}
"""

    payload = {
        "model": MODEL_NAME,
        "prompt": prompt,
        "stream": False
    }

    response = requests.post(OLLAMA_URL, json=payload)

    data = response.json()

    answer = data["response"]

    store_memory(db, message)
    store_memory(db, answer)

    return answer
