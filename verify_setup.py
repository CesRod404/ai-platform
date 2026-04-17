import os
import sys
from sqlalchemy import create_engine, text
from dotenv import load_dotenv
import google.generativeai as genai

# Setup environment
PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
load_dotenv(os.path.join(PROJECT_ROOT, "backend", ".env"))

def check_database():
    print("\n--- 1. Database Check (Supabase) ---")
    db_url = os.getenv("DATABASE_URL")
    if not db_url or "YOUR-PASSWORD" in db_url:
        print("❌ DATABASE_URL not set correctly in .env")
        return False
    
    if db_url.startswith("postgresql://"):
        db_url = db_url.replace("postgresql://", "postgresql+psycopg://", 1)
    
    try:
        engine = create_engine(db_url)
        with engine.connect() as conn:
            # Check vector extension
            result = conn.execute(text("SELECT name FROM pg_extension WHERE name = 'vector';"))
            if not result.fetchone():
                print("❌ Vector extension is NOT enabled in Supabase.")
                print("   👉 Run: CREATE EXTENSION IF NOT EXISTS vector; in SQL Editor.")
                return False
            
            # Check if memory table exists
            result = conn.execute(text("SELECT EXISTS (SELECT FROM information_schema.tables WHERE table_name = 'memory');"))
            if not result.fetchone()[0]:
                print("⚠️  'memory' table doesn't exist yet. Running migrations...")
                from app.db.database import Base
                from app.db import models
                Base.metadata.create_all(bind=engine)
                print("✅ Tables initialized.")
            else:
                print("✅ Database and tables are ready.")
        return True
    except Exception as e:
        print(f"❌ Database error: {str(e)}")
        return False

def check_gemini():
    print("\n--- 2. Gemini API Check ---")
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key or api_key == "your_gemini_api_key_here":
        print("❌ GEMINI_API_KEY is missing or invalid in .env")
        return False
    
    try:
        genai.configure(api_key=api_key)
        model = genai.GenerativeModel("gemini-1.5-flash")
        response = model.generate_content("Ping")
        if response.text:
            print("✅ Gemini API is working correctly.")
            return True
    except Exception as e:
        print(f"❌ Gemini API error: {str(e)}")
        return False

if __name__ == "__main__":
    db_ok = check_database()
    ai_ok = check_gemini()
    
    print("\n" + "="*30)
    if db_ok and ai_ok:
        print("🚀 EVERYTHING IS READY FOR DEPLOYMENT!")
    else:
        print("⚠️  Some things need your attention before deploying.")
    print("="*30)
