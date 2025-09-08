# All API routes. ----------------------------------------

# Imports FastAPI components for form/file handling and error responses
from fastapi import APIRouter

router = APIRouter()

@router.get("/")
def read_root():
    return {"message ": " Welcome to your project  🎉"}