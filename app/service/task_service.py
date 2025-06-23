from app.model.task_model import Task
from app.service.supabase_service import SupabaseService

class TaskService:

    @staticmethod
    def create_task(task: Task):
        return SupabaseService.create_task(task)

    @staticmethod
    def list_tasks():
        return SupabaseService.list_tasks()
