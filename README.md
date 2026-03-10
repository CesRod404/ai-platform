AI Platform – Local LLM Chat with Vector Memory
Overview

This project is a full-stack AI chat platform that runs a local Large Language Model (LLM) and stores conversation memory using vector embeddings. The system allows users to interact with an AI assistant while preserving contextual knowledge through a vector database.

The platform is built with a modern architecture combining a Python backend and a React frontend.

Main goals of this project:

Run AI models locally

Store conversation memory

Retrieve relevant context using vector similarity

Provide a modern chat interface

Architecture

The project follows a modular architecture:

ai-platform
│
├── backend
│   ├── app
│   │   ├── api
│   │   ├── db
│   │   ├── services
│   │   └── models
│   │
│   └── main.py
│
└── frontend
    ├── src
    └── components

Tech Stack

Backend

Python

FastAPI

SQLAlchemy

PostgreSQL

pgvector

SentenceTransformers

AI Model

Ollama

Qwen coder models

Frontend

React

JavaScript

CSS

Infrastructure

REST API

Vector database

Local AI inference

Features
Local LLM Integration

The platform integrates a local AI model through Ollama, allowing inference without relying on external APIs.

Benefits:

Full local control

No API costs

Private data processing

Chat API

The backend exposes a simple chat endpoint:

POST /chat


Example request:

{
  "message": "Hello AI"
}


Example response:

{
  "response": "Hello! How can I help you today?"
}

Vector Memory System

The platform includes a memory system based on embeddings.

Steps:

User sends a message

Message is converted into an embedding

Embedding is stored in the database

Relevant context is retrieved using vector similarity

Context is injected into the LLM prompt

This allows the AI to remember previous conversations.

Embedding Model

Embeddings are generated using:

all-MiniLM-L6-v2


from SentenceTransformers.

Example embedding generation:

from sentence_transformers import SentenceTransformer

model = SentenceTransformer("all-MiniLM-L6-v2")

def create_embedding(text: str):
    embedding = model.encode(text)
    return embedding.tolist()

Vector Database

The project uses:

PostgreSQL

pgvector

Database example:

ai_platform


Vectors are stored to allow semantic search across past conversations.

Backend API

Main API routes:

GET /
POST /chat


The backend is implemented using FastAPI.

Run the backend:

uvicorn app.main:app --reload


Server runs at:

http://127.0.0.1:8000

Frontend Chat Interface

The frontend is implemented using React and provides a minimal chat interface where users can:

send messages

receive responses

view conversation history

The frontend communicates with the backend using REST calls.

Running the Project
Backend

Install dependencies:

pip install -r requirements.txt


Run server:

uvicorn app.main:app --reload

Frontend

Install dependencies:

npm install


Start development server:

npm run dev

Environment Variables

Example .env file:

DATABASE_URL=postgresql://user:password@localhost/ai_platform

AI Model Setup

Install Ollama and download a model:

ollama run qwen2.5-coder:7b


This model is used as the local LLM for the platform.

Future Improvements

Possible future improvements:

authentication system

multi-user memory

conversation threads

streaming responses

better chat UI

knowledge base ingestion

document embeddings

Learning Outcomes

This project demonstrates practical knowledge of:

building AI powered applications

LLM integration

vector databases

semantic search

full stack development

local AI infrastructure

Author

César Rodríguez
Software Engineering Student
Junior Developer – AI & Web Developmen