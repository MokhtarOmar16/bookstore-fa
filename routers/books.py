from fastapi import APIRouter , Depends, HTTPException, Response, Query
from sqlalchemy.orm import Session
from core.database import get_db
from services.books import create_book, get_books
from schemas.books import BookCreateSchema, BookResponseSchema
from typing import Annotated
from utils.pagination.paginator import PaginateByPage
from utils.pagination.schema import PaginatationSchema

router = APIRouter(
    prefix="/books",
    tags=["books"],
)


@router.post("/", response_model=BookResponseSchema)
def create_book_endpoint(book: BookCreateSchema, db: Session = Depends(get_db)):
    return create_book(db, book)


@router.get("", response_model=PaginatationSchema[BookResponseSchema])
def list_books(
    paginator: Annotated[PaginateByPage, Depends()],
    db:Annotated[Session, Depends(get_db)]
    ):
    
    return get_books(db, paginator)