from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, DeclarativeBase, Mapped, mapped_column




engine = create_engine('sqlite:///./store.db', connect_args={"check_same_thread": False})
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

class Base(DeclarativeBase):
    id: Mapped[int] = mapped_column(primary_key=True)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
