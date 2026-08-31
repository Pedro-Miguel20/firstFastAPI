from fastapi import APIRouter, Depends
from app.db.database import AsyncSessionLocal
from app.models.todo import TodoCreate, TodoResponse, TodoDelete
from app.services.todo_service import TodoService


router = APIRouter()

async def get_todo_service():
    session=AsyncSessionLocal()
    try:
        # Pass the active session to the service
        yield TodoService(session=session)
    finally:
        # Automatically executes AFTER the router finishes returning the response
        await session.close()

@router.get("/todos", response_model=list[TodoResponse])
async def get_todos(service: TodoService = Depends(get_todo_service)):
    return await service.list_todo()

@router.get("/todos/{todo_id}", response_model=TodoResponse)
async def get_todo(todo_id: int, service: TodoService = Depends(get_todo_service)):
    return service.get_todo(todo_id)

@router.post("/todos", response_model=TodoCreate)
async def create_todo(todo: TodoCreate, service: TodoService = Depends(get_todo_service)):
    return service.create_todo(todo)

@router.delete("/todos/{todo_id}", response_model=TodoDelete)
async def delete_todo(todo_id: int, service: TodoService = Depends(get_todo_service)):
    return service.delete_todo(todo_id)