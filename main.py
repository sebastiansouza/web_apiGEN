from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from . import crud, models, schemas
from config.database import SessionLocal, engine

app = FastAPI()

# Configurando o banco de dados
models.Base.metadata.create_all(bind=engine)

# Função auxiliar para obter a sessão do banco de dados
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Rotas para operações CRUD de usuários

@app.post("/users/")
def create_user(user: schemas.UserCreate, db: Session = Depends(get_db)):
    return crud.create_user(db=db, user=user)

@app.get("/users/{user_id}")
def read_user(user_id: int, db: Session = Depends(get_db)):
    db_user = crud.get_user(db=db, user_id=user_id)
    if db_user is None:
        raise HTTPException(status_code=404, detail="User not found")
    return db_user

@app.put("/users/{user_id}")
def update_user(user_id: int, user: schemas.UserUpdate, db: Session = Depends(get_db)):
    return crud.update_user(db=db, user_id=user_id, user_data=user)

@app.delete("/users/{user_id}")
def delete_user(user_id: int, db: Session = Depends(get_db)):
    return crud.delete_user(db=db, user_id=user_id)


# Rotas para operações CRUD de postagens

@app.post("/posts/")
def create_post(post: schemas.PostCreate, db: Session = Depends(get_db)):
    return crud.create_post(db=db, post=post)

@app.get("/posts/{post_id}")
def read_post(post_id: int, db: Session = Depends(get_db)):
    db_post = crud.get_post(db=db, post_id=post_id)
    if db_post is None:
        raise HTTPException(status_code=404, detail="Post not found")
    return db_post

@app.put("/posts/{post_id}")
def update_post(post_id: int, post: schemas.PostUpdate, db: Session = Depends(get_db)):
    return crud.update_post(db=db, post_id=post_id, post_data=post)

@app.delete("/posts/{post_id}")
def delete_post(post_id: int, db: Session = Depends(get_db)):
    return crud.delete_post(db=db, post_id=post_id)


# Rotas para operações CRUD de temas

@app.post("/themes/")
def create_theme(theme: schemas.ThemeCreate, db: Session = Depends(get_db)):
    return crud.create_theme(db=db, theme=theme)

@app.get("/themes/{theme_id}")
def read_theme(theme_id: int, db: Session = Depends(get_db)):
    db_theme = crud.get_theme(db=db, theme_id=theme_id)
    if db_theme is None:
        raise HTTPException(status_code=404, detail="Theme not found")
    return db_theme

@app.put("/themes/{theme_id}")
def update_theme(theme_id: int, theme: schemas.ThemeUpdate, db: Session = Depends(get_db)):
    return crud.update_theme(db=db, theme_id=theme_id, theme_data=theme)

@app.delete("/themes/{theme_id}")
def delete_theme(theme_id: int, db: Session = Depends(get_db)):
    return crud.delete_theme(db=db, theme_id=theme_id)
