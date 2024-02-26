from sqlalchemy.orm import Session
from app.models.post_models import Post
from app.schemas.post_schema import PostCreate, PostUpdate
from typing import List


def get_post(db: Session, post_id: int):
    return db.query(Post).filter(Post.id == post_id).first()


def get_posts(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Post).offset(skip).limit(limit).all()


def create_post(db: Session, post: PostCreate):
    db_post = Post(**post.dict())
    db.add(db_post)
    db.commit()
    db.refresh(db_post)
    return db_post


def update_post(db: Session, post_id: int, post: PostUpdate):
    db_post = db.query(Post).filter(Post.id == post_id).first()
    if db_post:
        for attr, value in vars(post).items():
            setattr(db_post, attr, value) if value else None
        db.commit()
        db.refresh(db_post)
    return db_post


def delete_post(db: Session, post_id: int):
    db_post = db.query(Post).filter(Post.id == post_id).first()
    if db_post:
        db.delete(db_post)
        db.commit()
        return db_post


def get_posts_by_user(db: Session, user_id: int) -> List[Post]:
    return db.query(Post).filter(Post.user_id == user_id).all()


def get_posts_by_theme(db: Session, theme_id: int) -> List[Post]:
    return db.query(Post).filter(Post.theme_id == theme_id).all()
