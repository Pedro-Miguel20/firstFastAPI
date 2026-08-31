from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession
from app.db.schema import Todo
from app.models.todo import TodoCreate

class TodoService():
    def __init__ (self, session: AsyncSession):
        self.session = session    

    async def list_todo(self) -> list[Todo]:
        stmt = select(Todo)
        
        # 2. Executa a busca de forma assíncrona
        result = await self.session.execute(stmt)
        
        # 3. Retorna os objetos mapeados como uma lista
        return list(result.scalars().all())

    def get_todo(self, todo_id: int) -> Todo | None:
        return self.session.query(Todo).filter(Todo.id == todo_id).first()

    def create_todo(self, todo: TodoCreate) -> Todo:
        todo_data = Todo(**todo.model_dump())

        self.session.add(todo_data)
        self.session.commit()
        self.session.refresh(todo_data)
        return todo_data

    def delete_todo(self, todo_id: int) -> Todo:
        todo = self.session.query(Todo).filter(Todo.id == todo_id).first()

        if todo:
            todo.active = not todo.active
            self.session.commit()
            self.session.refresh(todo)
        return todo
