from locust import HttpUser, between, SequentialTaskSet, task, events
from db.database import AsyncSessionLocal
import asyncio
from sqlalchemy import text
from datetime import datetime, timezone,timedelta
from itertools import count

counter = count(1)

class todoWorkFlow(SequentialTaskSet):
    todo_id = None
    # 3. Tarefa contínua executada pelos usuários virtuais

    @task
    def create_todo(self):

        dia = next(counter)


        data_obj = datetime.now(timezone.utc) + timedelta(days=dia)
                
                # 2. Converte para o padrão ISO sem o sufixo +00:00
        data_string = data_obj.replace(tzinfo=None).isoformat(timespec='seconds')

        response = self.client.post("/todos", json={
            "title": f"teste",
            "description": f"testando",
            "due_datetime":  data_string,
            "done": False
        })
        if response.status_code == 200:
            self.todo_id = response.json()["id"]


    @task
    def get_todo(self):
        if self.todo_id:
            self.client.get(f"/todos/{self.todo_id}", name="/todos/[get_id]")

    @task 
    def delete_todo(self):
        if self.todo_id:
            self.client.delete(f"/todos/{self.todo_id}", name="/todos/[delete_id]")


class TodoTest(HttpUser):
    wait_time = between(1, 5)
    tasks = [todoWorkFlow]

@events.test_stop.add_listener
def cleanup_database(environment, **kwargs):
    print("\n[CLEANUP] Teste finalizado. Limpando dados remanescentes no banco...")
    
    # Exemplo: Se sua API tiver uma rota de expurgo/reset
    async def run_cleanup():
        async with AsyncSessionLocal() as session:
            # 1. Executa o Hard Delete usando a instrução textual explícita
            await session.execute(text("DELETE FROM public.todo;"))
            
            # 2. Faz o commit para efetivar a remoção física no Postgres
            await session.commit()

    try:
        asyncio.run(run_cleanup())
        print("[CLEANUP] Registros apagados fisicamente com sucesso!")
        
    except Exception as e:
        print(f"[CLEANUP] Erro ao limpar o banco: {e}")




      

    