# database.py
# Handles the connection to our SQLite database

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base

# SQLite database file — will be auto-created as todos.db
DATABASE_URL = "sqlite:///./todos.db"

# Create the database engine
engine = create_engine(
    DATABASE_URL,
    connect_args={"check_same_thread": False}  # SQLite-specific requirement
)

# Each request gets its own database session through this
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# All models will inherit from this Base class
Base = declarative_base()


def get_db():
    """
    Dependency function — gives each request a database session
    and closes it cleanly when the request finishes.
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()