from pydantic import BaseModel
from typing import List, Optional
from datetime import datetime
from .post_schema import Post 

class ThemeBase(BaseModel):
    description: str

class ThemeCreate(ThemeBase):
    pass

class ThemeUpdate(ThemeBase):
    pass

class Theme(ThemeBase):
    id: int
    posts: Optional[List[Post]] = []

    class Config:
        from_attributes = True
