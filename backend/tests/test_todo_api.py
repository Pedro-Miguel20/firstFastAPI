from services.todo_service import TodoService
from models.todo import TodoCreate, TodoResponse
import pytest
from db.database import AsyncSessionLocal
from pydantic import ValidationError
from datetime import datetime, timezone, timedelta
from db.database import engine


get : TodoResponse = None

@pytest.mark.asyncio
async def test_pydantic():
    
    
    payload = {
        "title": "Pytest",
        "description": "Pytest",
        "due_datetime": "datastromg",
        "done": False,
    }

    with pytest.raises(ValidationError):
        TodoCreate(**payload)


@pytest.mark.asyncio
async def test_create_and_get_todo():

    data_obj = datetime.now(timezone.utc) + timedelta(days=1)
                    
                    # 2. Converte para o padrão ISO sem o sufixo +00:00
    data_string = data_obj.replace(tzinfo=None)
    
    todo = TodoCreate(
        title="Pytest",
        description="Pytest",
        due_datetime= data_string,
        done=False,
    )  
    
    async with AsyncSessionLocal() as session:
        service = TodoService(session=session)

        result : TodoResponse = await service.create_todo(todo=todo)

        response = await service.get_todo(todo_id=result.id)

        assert response.id == result.id
        assert response.title == todo.title
        assert response.description == todo.description
        assert response.done == todo.done

        global get

        get = result

        await engine.dispose()

@pytest.mark.asyncio
async def test_list_todo():

    async with AsyncSessionLocal() as session:
        service = TodoService(session=session)
                
        response = await service.list_todo()

        assert len(response) >= 1

        await engine.dispose()
        

        
@pytest.mark.asyncio
async def test_delete_todo():

    async with AsyncSessionLocal() as session:
        service = TodoService(session=session)

        
        after = await service.delete_todo(todo_id=get.id)

        assert get.active != after.active
        assert after.completed_at is None

        await engine.dispose()

        
@pytest.mark.asyncio
async def test_edit_todo():

    async with AsyncSessionLocal() as session:
        service = TodoService(session=session)

        
        after = await service.done_todo(todo_id=get.id)

        assert get.done != after.done
        assert after.completed_at is not None