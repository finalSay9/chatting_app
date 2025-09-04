from numbers import Number
from fastapi import FastAPI, Depends, APIRouter, HTTPException
from sqlalchemy.orm import Session
from models import User
from database import SessionLocal, engine, Base
from routes import chat, users, messages
from fastapi.middleware.cors import CORSMiddleware
import routes.auth


app = FastAPI(title='Messeging Application')

Base.metadata.create_all(bind=engine)

app.include_router(users.router, tags=["users"])
app.include_router(routes.auth.router, tags=['auth'])
app.include_router(messages.router, tags=['messages'])
app.include_router(chat.router, tags=['chat'])


# CORS middleware to allow frontend to communicate with the backend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, replace with actual frontend domain
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

        


