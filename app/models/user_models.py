from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from ..database import Base

class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    email = Column(String, unique=True, index=True)
    photo = Column(String)

    # Relacionamento com as postagens
    posts = relationship("Post", back_populates="author")
