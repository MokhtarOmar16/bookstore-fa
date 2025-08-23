from pydantic import BaseModel
from typing import TypeVar , Generic

T = TypeVar("T", bound=BaseModel)

class PaginatationSchema(BaseModel, Generic[T]):
    page: int
    page_size: int
    total_pages: int
    total_items: int
    items: list[T]