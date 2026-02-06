from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

from fastapi import FastAPI

app = FastAPI()

DATABASE_URL = "sqlite:///./test.db"

engine = create_engine(DATABASE_URL, connect_args*{"check_same_thread": False})
SessionLocal =sessionmaker(autocommit= False, autoflush= False, bind=engine)
Base = declarative_base()
class user(Base):
    __tablename__ ="users"

    id= Column(Integer, primary_key= True, index =True)
    name =Column(String, Index = True)
    email = Column(String, unique =True, Index =True)
Base.metadata.create_all(bind= engine)





from sqlalchemy.orm import session

def get_db():
    db = SessionLocal
    try:
        yield db
    finally:
        db.close()
