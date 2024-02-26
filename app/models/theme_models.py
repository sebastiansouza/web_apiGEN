from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship

from ..database import Base

class Theme(Base):
    __tablename__ = "themes"

    id = Column(Integer, primary_key=True, index=True)
    description = Column(String, index=True)

    # Relacionamento com as postagens
    posts = relationship("Post", back_populates="theme")
