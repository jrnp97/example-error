import time
from locust import HttpUser, task, between

class QuickstartUserTwo(HttpUser):
    wait_time = between(1, 5)

    @task
    def view_items(self):
        print("dummy_task_two")


