from services.todo_service import TodoService
from models.todo import TodoCreate
import pytest
from db.database import AsyncSessionLocal
from pydantic import ValidationError
from datetime import datetime, timezone, timedelta
import asyncio

def test_create_todo():

    data_obj = datetime.now(timezone.utc) + timedelta(days=1)
                    
                    # 2. Converte para o padrão ISO sem o sufixo +00:00
    data_string = data_obj.replace(tzinfo=None).isoformat(timespec='seconds')
    
    payload = {
                "title": "Pytest",
                "description": "Pytest",
                "due_datetime": data_string,
                "done":  False
    }

    todo = TodoCreate(**payload)

    async def run():
        async with AsyncSessionLocal() as session:
            service = TodoService(session=session)

            return await service.create_todo(todo=todo)
    
    result = asyncio.run(run())

    assert result.title == payload['title']

def test_pydantic():
    
    payload = {
                "title": "Pytest",
                "description": "Pytest",
                "due_datetime": "data_string",
                "done":  False
    }

    with pytest.raises(ValidationError):
        print(ValidationError)
        TodoCreate(**payload)

def test_get_todo():
    async def list():
        async with AsyncSessionLocal() as session:
            service = TodoService(session=session)

            return await service.list_todo()
    
    asyncio.run(list())

    
    
