from pydantic import BaseModel, EmailStr
from datetime import datetime
from typing import Optional


# --------- Auth Schemas ---------
class Token(BaseModel):
    access_token: str
    token_type: str


class TokenData(BaseModel):
    email: Optional[str] = None


# --------- User Schemas ---------
class UserCreate(BaseModel):
    name: str
    email: EmailStr
    phone: str
    password: str


class UserResponse(BaseModel):
    id: int
    name: str
    email: str
    phone: str

    class Config:
        from_attributes = True  # allows ORM to Pydantic conversion


# --------- Message Schemas ---------
class MessageCreate(BaseModel):
    receiver_id: int
    content: str
    # timestamp is usually set by backend, so optional
    timestamp: Optional[datetime] = None
    is_read: bool = False  # default unread


class MessageResponse(BaseModel):
    id: int
    sender_id: int
    receiver_id: int
    content: str
    timestamp: datetime
    is_read: bool


# --------- Chat Schemas ---------
class ChatCreate(BaseModel):
    name: str


class ChatResponse(BaseModel):
    id: int
    name: str
    created_at: datetime
