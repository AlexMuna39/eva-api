from fastapi import APIRouter
from app.route import healthcheck, task_route

router = APIRouter()

# Include all routers here
router.include_router(healthcheck.router)
router.include_router(task_route.router)
