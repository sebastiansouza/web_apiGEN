from sqlalchemy import Column, Integer, String, ForeignKey, DateTime
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

class User(Base):
    __tablename__ = 'users'  

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, index=True)  
    email = Column(String, unique=True, index=True)
    foto = Column(String)

    posts = relationship("Post", back_populates="author", lazy='select')

class Post(Base):
    __tablename__ = 'posts'

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String)  
    content = Column(String)   
    date = Column(DateTime)
    user_id = Column(Integer, ForeignKey('users.id')) 
    theme_id = Column(Integer, ForeignKey('themes.id')) 
    
    author = relationship("User", back_populates="posts")

    
    theme = relationship("Theme", back_populates="posts")

class Theme(Base):
    __tablename__ = 'themes'

    id = Column(Integer, primary_key=True, index=True)
    description = Column(String) 

    
    posts = relationship("Post", back_populates="theme", lazy='select')
