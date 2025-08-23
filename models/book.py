from sqlalchemy import ForeignKey, String
from sqlalchemy.orm import Mapped, mapped_column, relationship
from core.database import Base
from typing import List


class Book(Base):
    __tablename__ = "books"

    title: Mapped[str] = mapped_column(String(100), nullable=False)
    description: Mapped[str] = mapped_column(String(250), nullable=True)
    author_id: Mapped[int] = mapped_column(ForeignKey("authors.id"), nullable=False)
    author : Mapped["Author"] = relationship("Author", back_populates="books")
    reviews: Mapped[List["Review"]] = relationship("Review", back_populates="book", cascade="all, delete-orphan")


