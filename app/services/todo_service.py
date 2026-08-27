from sqlalchemy.orm import Session

from app.db.schema import Todo
from app.models.todo import TodoCreate

class TodoService():
    def __init__ (self, session: Session):
        self.session = session    

    def list_todo(self) -> list[Todo]:
        return self.session.query(Todo).all()

    def get_todo(self, todo_id: int) -> Todo | None:
        return self.session.query(Todo).filter(Todo.id == todo_id).first()

    def create_todo(self, todo: TodoCreate) -> Todo:
        todo_data = Todo(**todo.model_dump())

        self.session.add(todo_data)
        self.session.commit()
        self.session.refresh(todo_data)
        return todo_data
