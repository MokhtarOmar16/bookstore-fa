from sqlalchemy import String
from sqlalchemy.orm import Mapped, mapped_column, relationship

from core.database import Base



class Author(Base):
    __tablename__ = "authors"

    name: Mapped[str] = mapped_column(String(100), nullable=False)
    biography: Mapped[str] 
    books: Mapped[list["Book"]] = relationship("Book", back_populates="author")