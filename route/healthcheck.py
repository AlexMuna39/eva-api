from fastapi import APIRouter

router = APIRouter()

@router.get("/health")
def healthcheck():
    return {"message": "Eva's API is alive!"}
