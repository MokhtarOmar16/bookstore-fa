from sqlalchemy.orm import Session
from sqlalchemy import select
from models import Book
from schemas.books import BookCreateSchema, BookResponseSchema
from utils.pagination import PaginateByPage


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


def get_books(db: Session, paginator: PaginateByPage) -> list[BookResponseSchema]:
    stmt = select(Book).offset(paginator.skip).limit(paginator.page_size)
    return db.scalars(stmt).all()