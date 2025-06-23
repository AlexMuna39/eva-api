from fastapi import APIRouter
from app.routes import healthcheck, task_routes

router = APIRouter()

# Include all routers here
router.include_router(healthcheck.router)
router.include_router(task_routes.router)
