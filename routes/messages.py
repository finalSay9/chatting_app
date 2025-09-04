from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
import models, schema
from database import get_db
from routes.auth import get_current_user


router = APIRouter(prefix="/messages", tags=["messages"])


# Send a message
@router.post("/", response_model=schema.MessageResponse)
def send_message(
    message: schema.MessageCreate,
    db: Session = Depends(get_db),
    current_user: models.User = Depends(get_current_user)
):
    db_message = models.Message(
        sender_id=current_user.id,
        receiver_id=message.receiver_id,
        content=message.content
    )
    db.add(db_message)
    db.commit()
    db.refresh(db_message)
    return db_message


# Get all messages between two users
@router.get("/{other_user_id}", response_model=list[schema.MessageResponse])
def get_messages(
    other_user_id: int,
    db: Session = Depends(get_db),
    current_user: models.User = Depends(get_current_user)
):
    messages = db.query(models.Messages).filter(
        ((models.Messages.sender_id == current_user.id) & (models.Messages.receiver_id == other_user_id)) |
        ((models.Messages.sender_id == other_user_id) & (models.Messages.receiver_id == current_user.id))
    ).order_by(models.Messages.timestamp).all()

    return messages