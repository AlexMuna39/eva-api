from fastapi import APIRouter
from typing import List
from app.models.task import Task
from app.services import task_service

router = APIRouter(prefix="/tasks", tags=["Tasks"])

@router.get("/", response_model=List[Task])
def get_tasks():
    return task_service.list_tasks()

@router.post("/", response_model=Task)
def create_task(task: Task):
    new_task = task_service.add_task(task.dict())
    return new_task
