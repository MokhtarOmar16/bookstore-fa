from fastapi import APIRouter , Depends, HTTPException, Response, Query
from core.database import get_db
import models


router = APIRouter(
    prefix="/books",
    tags=["books"],
)

