from pydantic import BaseModel
from fastapi import Query
from core.config_loader import get_settings


settings = get_settings()


class PaginateByPage(BaseModel):
    page: int = Query(1, ge=1, description="Page number")
    page_size: int = Query(settings.PAGE_SIZE  ,ge=1, le=100, description="Number of items per page")
    
    
    @property
    def skip(self) -> int:
        return (self.page - 1) * self.page_size

    @property
    def limit(self) -> int:
        return self.page_size

