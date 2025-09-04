from numbers import Number
from fastapi import FastAPI, Depends, APIRouter, HTTPException
from sqlalchemy.orm import Session
from models import User
from database import SessionLocal, engine, Base
from routes import users, messages
from fastapi.middleware.cors import CORSMiddleware
import routes.auth


app = FastAPI(title='Messeging Application')

Base.metadata.create_all(bind=engine)

app.include_router(users.router, tags=["users"])
app.include_router(routes.auth.router, tags=['auth'])
app.include_router(messages.router, tags=['messages'])



        


