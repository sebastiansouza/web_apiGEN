from sqlalchemy.orm import Session
from . import models, schemas

def get_user(db: Session, user_id: int):
    return db.query(models.User).filter(models.User.id == user_id).first()

def get_users(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.User).offset(skip).limit(limit).all()

def create_user(db: Session, user: schemas.UserCreate):
    db_user = models.User(**user.dict())
    db.add(db_user)
    db.commit()
    db.refresh(db_user)
    return db_user

def update_user(db: Session, user_id: int, user_data: schemas.UserUpdate):
    db_user = db.query(models.User).filter(models.User.id == user_id).first()
    for key, value in user_data.dict().items():
        setattr(db_user, key, value)
    db.commit()
    db.refresh(db_user)
    return db_user

def delete_user(db: Session, user_id: int):
    db_user = db.query(models.User).filter(models.User.id == user_id).first()
    db.delete(db_user)
    db.commit()


def get_post(db: Session, post_id: int):
    return db.query(models.Postagem).filter(models.Postagem.id == post_id).first()

def get_posts(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Postagem).offset(skip).limit(limit).all()

def create_post(db: Session, post: schemas.PostagemCreate):
    db_post = models.Postagem(**post.dict())
    db.add(db_post)
    db.commit()
    db.refresh(db_post)
    return db_post

def update_post(db: Session, post_id: int, post_data: schemas.PostagemUpdate):
    db_post = db.query(models.Postagem).filter(models.Postagem.id == post_id).first()
    for key, value in post_data.dict().items():
        setattr(db_post, key, value)
    db.commit()
    db.refresh(db_post)
    return db_post

def delete_post(db: Session, post_id: int):
    db_post = db.query(models.Postagem).filter(models.Postagem.id == post_id).first()
    db.delete(db_post)
    db.commit()

def get_tema(db: Session, tema_id: int):
    return db.query(models.Tema).filter(models.Tema.id == tema_id).first()

def get_temas(db: Session, skip: int = 0, limit: int = 10):
    return db.query(models.Tema).offset(skip).limit(limit).all()

def create_tema(db: Session, tema: schemas.TemaCreate):
    db_tema = models.Tema(**tema.dict())
    db.add(db_tema)
    db.commit()
    db.refresh(db_tema)
    return db_tema

def update_tema(db: Session, tema_id: int, tema_data: schemas.TemaUpdate):
    db_tema = db.query(models.Tema).filter(models.Tema.id == tema_id).first()
    for key, value in tema_data.dict().items():
        setattr(db_tema, key, value)
    db.commit()
    db.refresh(db_tema)
    return db_tema

def delete_tema(db: Session, tema_id: int):
    db_tema = db.query(models.Tema).filter(models.Tema.id == tema_id).first()
    db.delete(db_tema)
    db.commit()
