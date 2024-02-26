from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class PostBase(BaseModel):
    title: str
    text: str
    created_at: Optional[datetime] = None
    user_id: int
    theme_id: int

class PostCreate(PostBase):
    pass

class PostUpdate(PostBase):
    pass

class Post(PostBase):
    id: int

    class Config:
        from_attributes = True
