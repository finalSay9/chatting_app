from datetime import datetime
from sqlalchemy import Boolean, Column, DateTime, ForeignKey, Integer, String
from database import Base  # your SQLAlchemy Base
from sqlalchemy.orm import relationship

class Message(Base):
    __tablename__ = "messages"

    id = Column(Integer, primary_key=True, index=True)
    sender_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    receiver_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    content = Column(String, nullable=False)
    timestamp = Column(DateTime, default=datetime.utcnow)
    is_read = Column(Boolean, default=False)


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True, nullable=False)
    phone = Column(String, nullable=False)
    password = Column(String, nullable=False)

    # Relationships AFTER Message is defined
    sent_messages = relationship("Message", foreign_keys=[Message.sender_id], back_populates="sender")
    received_messages = relationship("Message", foreign_keys=[Message.receiver_id], back_populates="receiver")

# Back-populates need to be added after both are known
Message.sender = relationship("User", foreign_keys=[Message.sender_id], back_populates="sent_messages")
Message.receiver = relationship("User", foreign_keys=[Message.receiver_id], back_populates="received_messages")


class ChatRoom(Base):
    __tablename__ = "chatrooms"  # always define __tablename__

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)
    created_at = Column(DateTime, default=datetime.utcnow)
