from sqlalchemy.orm import Session
from schemas.authors import AuthorCreateSchema, AuthorResponseSchema
from models import Author


def create_author(db: Session, author: AuthorCreateSchema) -> AuthorResponseSchema:
    db_author = Author(
        name=author.name,
        biography=author.biography
    )
    db.add(db_author)
    db.commit()
    db.refresh(db_author)
    return AuthorResponseSchema.model_validate(db_author)


def get_authors(db: Session) -> list[AuthorResponseSchema]:
    authors = db.query(Author).all()
    return [AuthorResponseSchema.model_validate(author) for author in authors]