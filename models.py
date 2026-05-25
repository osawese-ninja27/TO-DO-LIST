# models.py
# Defines the shape of our database table

from sqlalchemy import Column, Integer, String, Boolean, DateTime
from sqlalchemy.sql import func
from database import Base


class Todo(Base):
    __tablename__ = "todos"  # Name of the table in todos.db

    id          = Column(Integer, primary_key=True, index=True)
    title       = Column(String(200), nullable=False)
    description = Column(String(500), nullable=True)
    completed   = Column(Boolean, default=False)
    created_at  = Column(
        DateTime(timezone=True),
        server_default=func.now()
    )