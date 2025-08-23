from pydantic import BaseModel, ConfigDict



class BookCreateSchema(BaseModel):
    title: str
    description: str | None = None
    author_id: int


class BookResponseSchema(BaseModel):
    model_config = ConfigDict(from_attributes=True)

    id: int
    title: str
    description: str | None = None
    author_id: int

