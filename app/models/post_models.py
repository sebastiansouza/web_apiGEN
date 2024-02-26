from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from datetime import datetime

from ..database import Base

class Post(Base):
    __tablename__ = "posts"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    text = Column(String)
    created_at = Column(DateTime, default=datetime.utcnow)
    user_id = Column(Integer, ForeignKey("users.id"))
    theme_id = Column(Integer, ForeignKey("themes.id"))  

    # Relacionamento com o usuário
    author = relationship("User", back_populates="posts")

    # Relacionamento com o tema
    theme = relationship("Theme", back_populates="posts")
