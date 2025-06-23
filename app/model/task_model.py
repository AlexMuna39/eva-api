from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class Task(BaseModel):
    id: int
    title: str
    description: Optional[str] = None
    created_at: datetime
    completed: bool = False
    
