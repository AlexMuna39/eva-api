from fastapi import APIRouter
from app.model.task_model import Task
from app.service.task_service import TaskService

router = APIRouter()

@router.get("/tasks", response_model=list[Task])
def get_tasks():
    return TaskService.list_tasks()

@router.post("/tasks", response_model=Task)
def create_task(task: Task):
    return TaskService.create_task(task)
