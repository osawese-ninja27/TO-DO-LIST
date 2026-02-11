from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from pydantic import BaseModel

from fastapi import FastAPI, Depends

app = FastAPI()

DATABASE_URL = "sqlite:///./test.db"

engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})
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

class UserCreate(BaseModel):
    name: str
    email: str

@app.post("/users/", response_model= user)
def create_user(user:UserCreate, db: session=Depends(get_db)):
    db_user = user(name= user.name, email =user.email)
    db.add(db_user) 
    db.commit
    db.refresh(db_user) 
    return db_user

