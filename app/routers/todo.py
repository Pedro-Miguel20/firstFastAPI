from fastapi import APIRouter, Depends
from app.db.schema import SessionLocal
from app.models.todo import TodoCreate, TodoResponse
from app.services.todo_service import TodoService


router = APIRouter()

def get_todo_service():
    session=SessionLocal()
    try:
        # Pass the active session to the service
        yield TodoService(session=session)
    finally:
        # Automatically executes AFTER the router finishes returning the response
        session.close()

@router.get("/todos", response_model=list[TodoResponse])
def get_todos(service: TodoService = Depends(get_todo_service)):
    return service.list_todo()

@router.get("/todos/{todo_id}", response_model=TodoResponse)
def get_todo(todo_id: int, service: TodoService = Depends(get_todo_service)):
    return service.get_todo(todo_id)

@router.post("/todos", response_model=TodoCreate)
def create_todo(todo: TodoCreate, service: TodoService = Depends(get_todo_service)):
    return service.create_todo(todo)