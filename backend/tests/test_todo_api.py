from services.todo_service import TodoService
from models.todo import TodoCreate, TodoResponse
import pytest
from db.database import AsyncSessionLocal
from pydantic import ValidationError
from datetime import datetime, timezone, timedelta

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

    @pytest.mark.asyncio
    async def run():
        async with AsyncSessionLocal() as session:
            service = TodoService(session=session)

            result = await service.create_todo(todo=todo, response_model=TodoResponse)

            result.title == payload['title']

def test_pydantic():
    
    payload = {
                "title": "Pytest",
                "description": "Pytest",
                "due_datetime": "data_string",
                "done":  False
    }

    @pytest.mark.asyncio
    async def run():
        async with AsyncSessionLocal() as session:
            service = TodoService(session=session)
            with pytest.raises(ValidationError):
                await service.create_todo(todo=payload)


def test_list_todo():

    @pytest.mark.asyncio
    async def run():
        async with AsyncSessionLocal() as session:
            service = TodoService(session=session)
                    
            response = await service.list_todo()

            assert len(response) >= 1

    
    
