from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session
from typing import List

from app.schemas.theme_schema import ThemeCreate, ThemeUpdate, Theme
from app.crud import theme_crud
from app.database import SessionLocal

router = APIRouter()

# Função auxiliar para obter a sessão do banco de dados
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/themes/", response_model=Theme)
def create_theme(theme: ThemeCreate, db: Session = Depends(get_db)):
    return theme_crud.create_theme(db=db, theme=theme)

@router.get("/themes/", response_model=List[Theme])
def read_themes(skip: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return theme_crud.get_themes(db=db, skip=skip, limit=limit)

@router.get("/themes/{theme_id}", response_model=Theme)
def read_theme(theme_id: int, db: Session = Depends(get_db)):
    db_theme = theme_crud.get_theme(db=db, theme_id=theme_id)
    if db_theme is None:
        raise HTTPException(status_code=404, detail="Theme not found")
    return db_theme

@router.put("/themes/{theme_id}", response_model=Theme)
def update_theme(theme_id: int, theme: ThemeUpdate, db: Session = Depends(get_db)):
    updated_theme = theme_crud.update_theme(db=db, theme_id=theme_id, theme=theme)
    if updated_theme is None:
        raise HTTPException(status_code=404, detail="Theme not found")
    return updated_theme

@router.delete("/themes/{theme_id}", response_model=Theme)
def delete_theme(theme_id: int, db: Session = Depends(get_db)):
    deleted_theme = theme_crud.delete_theme(db=db, theme_id=theme_id)
    if deleted_theme is None:
        raise HTTPException(status_code=404, detail="Theme not found")
    return deleted_theme
