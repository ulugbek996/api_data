from typing import Optional

from pydantic import BaseModel ,EmailStr
from datetime import datetime

class Data(BaseModel):
    id: int
    data: str
    time: str
    class Config:
        orm_mode = True

