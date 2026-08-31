from locust import HttpUser, task, between

class Test(HttpUser):
    wait_time = between(1, 3)

    @task
    def get_animals(self):
        self.client.get("/todos")