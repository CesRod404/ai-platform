from sqlalchemy import Column, Integer, Text, DateTime
from sqlalchemy.sql import func
from pgvector.sqlalchemy import Vector

from app.db.database import Base


class Memory(Base):

    __tablename__ = "memory"

    id = Column(Integer, primary_key=True, index=True)

    content = Column(Text)

    embedding = Column(Vector(384))

    created_at = Column(DateTime(timezone=True), server_default=func.now())
