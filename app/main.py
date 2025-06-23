from fastapi import FastAPI
from route import router
from route import healthcheck
from route import task_route

app = FastAPI()
app.include_router(router)
