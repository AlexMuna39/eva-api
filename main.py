from fastapi import FastAPI
from pydantic import BaseModel
from supabase import create_client
import os

app = FastAPI()

# Connect to Supabase using Replit Secrets
SUPABASE_URL = os.environ.get("SUPABASE_URL")
SUPABASE_KEY = os.environ.get("SUPABASE_KEY")
supabase = create_client(SUPABASE_URL, SUPABASE_KEY)


# Define the task structure
class Task(BaseModel):
    title: str
    context: str = ""
    status: str = "inbox"
    completed: bool = False


@app.post("/add_task")
async def add_task(task: Task):
    result = supabase.table("tasks").insert(task.dict()).execute()
    return {"status": "success", "result": result.data}
