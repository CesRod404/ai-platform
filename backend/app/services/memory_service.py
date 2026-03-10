from sqlalchemy.orm import Session
from app.db.models import Memory
from app.services.embedding_service import create_embedding


def store_memory(db: Session, text: str):

    embedding = create_embedding(text)

    memory = Memory(
        content=text,
        embedding=embedding
    )

    db.add(memory)
    db.commit()

def search_memory(db: Session, query: str):

    embedding = create_embedding(query)

    results = (
        db.query(Memory)
        .order_by(Memory.embedding.l2_distance(embedding))
        .limit(5)
        .all()
    )

    return [m.content for m in results]
