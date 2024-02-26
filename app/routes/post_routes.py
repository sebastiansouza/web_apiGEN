from fastapi import APIRouter, HTTPException, Depends, status
from sqlalchemy.orm import Session
from typing import List

from app.schemas.post_schema import PostCreate, PostUpdate, Post
from app.crud import post_crud
from app.database import SessionLocal

router = APIRouter()

# Função auxiliar para obter a sessão do banco de dados
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/posts/", status_code=status.HTTP_201_CREATED, response_model=Post)
def create_post(post: PostCreate, db: Session = Depends(get_db)):
    return post_crud.create_post(db=db, post=post)

@router.get("/posts/", status_code=status.HTTP_200_OK, response_model=List[Post])
def read_posts(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return post_crud.get_posts(db=db, skip=skip, limit=limit)

@router.get("/posts/{post_id}", status_code=status.HTTP_200_OK, response_model=Post)
def read_post(post_id: int, db: Session = Depends(get_db)):
    db_post = post_crud.get_post(db=db, post_id=post_id)
    if db_post is None:
        raise HTTPException(status_code=404, detail="Post not found")
    return db_post

@router.put("/posts/{post_id}", status_code=status.HTTP_200_OK, response_model=Post)
def update_post(post_id: int, post: PostUpdate, db: Session = Depends(get_db)):
    updated_post = post_crud.update_post(db=db, post_id=post_id, post=post)
    if updated_post is None:
        raise HTTPException(status_code=404, detail="Post not found")
    return updated_post

@router.delete("/posts/{post_id}", status_code=status.HTTP_200_OK, response_model=Post)
def delete_post(post_id: int, db: Session = Depends(get_db)):
    deleted_post = post_crud.delete_post(db=db, post_id=post_id)
    if deleted_post is None:
        raise HTTPException(status_code=404, detail="Post not found")
    return deleted_post
