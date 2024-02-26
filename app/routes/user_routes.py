from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from typing import List

from app.schemas.user_schema import UserCreate, UserUpdate, User
from app.crud import user_crud, post_crud
from app.database import SessionLocal

router = APIRouter()

# Função auxiliar para obter a sessão do banco de dados
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/users/", response_model=User)
def create_user(user: UserCreate, db: Session = Depends(get_db)):
    return user_crud.create_user(db=db, user=user)

@router.get("/users/", response_model=List[User])
def read_users(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    users = user_crud.get_users(db=db, skip=skip, limit=limit)
    
    # Para cada usuário, obtenha suas postagens
    for user in users:
        user.posts = post_crud.get_posts_by_user(db=db, user_id=user.id)
    
    return users

@router.get("/users/{user_id}", response_model=User)
def read_user(user_id: int, db: Session = Depends(get_db)):
    db_user = user_crud.get_user(db=db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    
    # Obter todas as postagens relacionadas a este usuário
    db_user.posts = post_crud.get_posts_by_user(db=db, user_id=user_id)
    
    return db_user

@router.put("/users/{user_id}", response_model=User)
def update_user(user_id: int, user: UserUpdate, db: Session = Depends(get_db)):
    updated_user = user_crud.update_user(db=db, user_id=user_id, user=user)
    if updated_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return updated_user

@router.delete("/users/{user_id}", response_model=User)
def delete_user(user_id: int, db: Session = Depends(get_db)):
    deleted_user = user_crud.delete_user(db=db, user_id=user_id)
    if deleted_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return deleted_user
