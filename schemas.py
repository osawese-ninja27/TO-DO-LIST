# schemas.py
# Pydantic schemas — validate data coming in and going out

from pydantic import BaseModel, Field
from typing import Optional
from datetime import datetime


class TodoCreate(BaseModel):
    """Schema for creating a new todo — sent by the client"""
    title: str = Field(
        ...,                    # ... means this field is required
        min_length=1,
        max_length=200
    )
    description: Optional[str] = Field(
        default=None,
        max_length=500
    )

    model_config = {
        "json_schema_extra": {
            "example": {
                "title": "Buy groceries",
                "description": "Milk, eggs, and bread"
            }
        }
    }


class TodoUpdate(BaseModel):
    """Schema for updating a todo — all fields optional"""
    title:       Optional[str]  = Field(default=None, min_length=1, max_length=200)
    description: Optional[str]  = Field(default=None, max_length=500)
    completed:   Optional[bool] = None


class TodoResponse(BaseModel):
    """Schema for returning a todo to the client"""
    id:          int
    title:       str
    description: Optional[str]
    completed:   bool
    created_at:  datetime

    model_config = {
        "from_attributes": True  # Lets Pydantic read SQLAlchemy model objects
    }