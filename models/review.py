from sqlalchemy import String , ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from core.database import Base


class Review(Base):
    __tablename__ = "reviews"

    content: Mapped[str] = mapped_column(String(500), nullable=False)
    rating: Mapped[int] = mapped_column(nullable=False)
    book_id: Mapped[int] = mapped_column(ForeignKey("books.id"), nullable=False)
    book: Mapped["Book"] = relationship("Book", back_populates="reviews")