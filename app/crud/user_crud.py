from sqlalchemy.orm import Session, joinedload
from app.models import user_models
from app.models.user_models import User
from app.schemas.user_schema import UserCreate, UserUpdate
from typing import List
from app.schemas.post_schema import Post 
from fastapi import HTTPException



def create_user(db: Session, user: UserCreate):
    # Verificar se o e-mail já está em uso
    if db.query(User).filter(User.email == user.email).first():
        raise HTTPException(status_code=409, detail="Email already registered")
    else:
        # Se o e-mail não estiver em uso, criar o usuário
        db_user = User(**user.model_dump())
        db.add(db_user)
        db.commit()
        db.refresh(db_user)
    return db_user


def get_users(db: Session, skip: int = 0, limit: int = 10):
    return db.query(User).offset(skip).limit(limit).options(joinedload(user_models.User.posts)).all()


def get_user(db: Session, user_id: int):
    return db.query(User).filter(User.id == user_id).first()


def update_user(db: Session, user_id: int, user: UserUpdate):
    db_user = db.query(User).filter(User.id == user_id).first()
    if db_user:
        for attr, value in vars(user).items():
            setattr(db_user, attr, value) if value else None
        db.commit()
        db.refresh(db_user)
    return db_user


def delete_user(db: Session, user_id: int):
    db_user = db.query(User).filter(User.id == user_id).first()
    if db_user:
        db.delete(db_user)
        db.commit()
        return db_user


def get_posts_by_user(db: Session, user_id: int) -> List[Post]:
    user = db.query(User).filter(User.id == user_id).first()
    if user:
        return user.posts
    else:
        return []
