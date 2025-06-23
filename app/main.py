from fastapi import FastAPI
from pydantic import BaseModel
from typing import List
from routes import healthcheck

app = FastAPI()
app.include_router(healthcheck.router, prefix="/health")

# Model for Tasks
class Task(BaseModel):
    id: int
    title: str
    description: str
    done: bool

# Dummy in-memory database
tasks: List[Task] = []

@app.get("/")
def read_root():
    return {"message": "Hello, this is Eva's Task Assistant API!"}

@app.get("/tasks")
def get_tasks():
    return tasks

@app.post("/tasks")
def create_task(task: Task):
    tasks.append(task)
    return task
