from datetime import datetime
from pydantic import BaseModel, ConfigDict

class TodoCreate(BaseModel):
    title: str
    description: str | None = None
    due_datetime: datetime
    completed_at: datetime
    done: bool = False

class TodoResponse(BaseModel):
    id: int
    title: str
    description: str
    due_datetime: datetime
    completed_at: datetime
    done: bool
    active: bool

    model_config = ConfigDict(from_attributes=True)
