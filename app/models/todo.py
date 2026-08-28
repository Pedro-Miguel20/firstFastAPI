from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field

class TodoCreate(BaseModel):
    title: str = Field(max_length=40)
    description: str | None = Field(max_length=200)
    due_datetime: datetime
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
