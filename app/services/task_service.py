from typing import List
from datetime import datetime
from app.models.task import Task

# In-memory database (temporary)
tasks: List[Task] = []

# Service functions
def add_task(task_data: dict) -> Task:
    task = Task(
        id=len(tasks) + 1,
        title=task_data["title"],
        description=task_data.get("description"),
        created_at=datetime.utcnow(),
        completed=False
    )
    tasks.append(task)
    return task

def list_tasks() -> List[Task]:
    return tasks
