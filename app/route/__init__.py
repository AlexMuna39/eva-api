from fastapi import APIRouter
from route import healthcheck, task_route

router = APIRouter()
router.include_router(healthcheck.router)
router.include_router(task_route.router)
