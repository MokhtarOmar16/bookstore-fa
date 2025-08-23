from sqlalchemy.orm import Session
from sqlalchemy import select, func
from math import ceil
from models import Book
from schemas.books import BookCreateSchema, BookResponseSchema
from utils.pagination.paginator import PaginateByPage
from utils.pagination.service import paginate


def create_book(db: Session, book: BookCreateSchema) -> BookResponseSchema:
    db_book = Book(
        title=book.title,
        description=book.description,
        author_id=book.author_id
    )
    db.add(db_book)
    db.commit()
    db.refresh(db_book)
    return db_book


def get_books(db: Session, paginator: PaginateByPage) -> dict:
    return paginate(db, select(Book), paginator)
