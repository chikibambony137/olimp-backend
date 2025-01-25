from fastapi import APIRouter, Depends
from database import get_db, Session
from models import *

router = APIRouter()

@router.get("/")
async def root():
    return {"message": "Welcome to the my API!"}
