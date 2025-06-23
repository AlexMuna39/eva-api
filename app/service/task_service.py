from app.model.task_model import Task

# Temporary in-memory storage
tasks_db = []

class TaskService:
    @staticmethod
    def create_task(task: Task):
        tasks_db.append(task)
        return task

    @staticmethod
    def list_tasks():
        return tasks_db
