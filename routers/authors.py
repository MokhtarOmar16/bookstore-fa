from sqlalchemy.orm import Session
from fastapi import APIRouter , Depends
from core.database import get_db
from schemas.authors import AuthorCreateSchema, AuthorResponseSchema
from services.authors import create_author

router = APIRouter(
    prefix="/authors",
    tags=["authors"],
)



@router.post("/", response_model=AuthorResponseSchema)
def createAuthor(author: AuthorCreateSchema, db: Session = Depends(get_db)):
    return create_author(db, author).model_dump()