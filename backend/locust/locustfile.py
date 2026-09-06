from locust import HttpUser, between, SequentialTaskSet, task, events
from sqlalchemy import text
from datetime import datetime, timezone,timedelta
from itertools import count
from core.config import settings


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



import psycopg2

def clear_database():
    database_url = settings.DATABASE_URL.replace(
        "postgresql+asyncpg://",
        "postgresql://"
    )

    with psycopg2.connect(database_url) as conn:
        with conn.cursor() as cursor:

            cursor.execute(
                "TRUNCATE TABLE public.todo RESTART IDENTITY"
            )

        conn.commit()

    print("[CLEANUP] Banco limpo!")


@events.test_stop.add_listener
def on_test_stop(environment, **kwargs):
    try:
        clear_database()
    except Exception as e:
        print(f"[CLEANUP] ERRO: {e}")