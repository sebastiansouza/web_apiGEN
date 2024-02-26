from sqlalchemy.orm import Session
from app.models.theme_models import Theme
from app.schemas.theme_schema import ThemeCreate, ThemeUpdate
from typing import List
from app.schemas.post_schema import Post 


def get_theme(db: Session, theme_id: int):
    return db.query(Theme).filter(Theme.id == theme_id).first()


def get_themes(db: Session, skip: int = 0, limit: int = 10):
    return db.query(Theme).offset(skip).limit(limit).all()


def create_theme(db: Session, theme: ThemeCreate):
    db_theme = Theme(**theme.dict())
    db.add(db_theme)
    db.commit()
    db.refresh(db_theme)
    return db_theme


def update_theme(db: Session, theme_id: int, theme: ThemeUpdate):
    db_theme = db.query(Theme).filter(Theme.id == theme_id).first()
    if db_theme:
        for attr, value in vars(theme).items():
            setattr(db_theme, attr, value) if value else None
        db.commit()
        db.refresh(db_theme)
    return db_theme


def delete_theme(db: Session, theme_id: int):
    db_theme = db.query(Theme).filter(Theme.id == theme_id).first()
    if db_theme:
        db.delete(db_theme)
        db.commit()
        return db_theme


def get_posts_by_theme(db: Session, theme_id: int) -> List[Post]:
    theme = db.query(Theme).filter(Theme.id == theme_id).first()
    if theme:
        return theme.posts
    else:
        return []
