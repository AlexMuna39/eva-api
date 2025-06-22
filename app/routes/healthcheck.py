from fastapi import APIRouter

router = APIRouter()

@router.get("/")
def healthcheck():
    return {"message": "Eva's API is alive!"}
