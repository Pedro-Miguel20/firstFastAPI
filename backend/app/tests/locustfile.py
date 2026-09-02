from locust import HttpUser, between, events, task
from itertools import count

counter = count(1)

class TodoTest(HttpUser):
    wait_time = between(1, 3)

    def on_start(self):
        # Armazena o ID do último todo criado por ESTE usuário específico
        self.last_todo_id = None 

    # 3. Tarefa contínua executada pelos usuários virtuais
    @task(1)
    def create_todo_task(self):
        i = next(counter)
        response = self.client.post("/todos", json={
            "title": f"teste{i}",
            "description": f"{i}",
            "due_datetime": "2026-10-01T16:18:02",
            "done": False
        })
        if response.status_code == 200:
            todo = self.client.get(f"/todos/{i}")
            print(todo)

      

    