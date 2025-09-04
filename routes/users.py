from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
import models, schema
from database import get_db
from routes.auth import get_current_user, get_password_hash

router = APIRouter(prefix="/users", tags=["users"])



@router.post("/register", response_model=schema.UserResponse)
def register_user(user_data: schema.UserCreate, db: Session = Depends(get_db)):
    db_user = db.query(models.User).filter(models.User.email == user_data.email).first()
    if db_user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Email already registered"
        )

    hashed_password = get_password_hash(user_data.password)
    db_user = models.User(
        name=user_data.name,
        email=user_data.email,
        phone=user_data.phone,
        password=hashed_password
    )
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

@router.get("/me", response_model=schema.UserResponse)
def read_users_me(current_user: models.User = Depends(get_current_user)):
    return current_user

@router.get("/{user_id}", response_model=schema.UserResponse)
def read_user(
    user_id: int,
    db: Session = Depends(get_db),
    current_user: models.User = Depends(get_current_user)
):
    user = db.query(models.User).filter(models.User.id == user_id).first()
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User not found"
        )
    return user

@router.get("/", response_model=list[schema.UserResponse])
def read_all_users(
    db: Session = Depends(get_db),
    current_user: models.User = Depends(get_current_user)
):
    return db.query(models.User).all()
