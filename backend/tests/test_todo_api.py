from models.todo import TodoCreate
import pytest
from pydantic import ValidationError

def test_create_todo():
    payload = {
                "title": "Pytest",
                "description": "Pytest",
                "due_datetime": "2026-02-02",
                "done": False
            }
    
    with pytest.raises(ValidationError):
        TodoCreate(json=payload)

    
    
