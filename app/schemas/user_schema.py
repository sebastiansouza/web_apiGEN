from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime
from .post_schema import Post 

class UserBase(BaseModel):
    name: str
    email: str
    photo: Optional[str] = None

class UserCreate(UserBase):
    pass

class UserUpdate(UserBase):
    pass

class User(UserBase):
    id: int
    posts: Optional[List[Post]] = []

    class Config:
        from_attributes = True
