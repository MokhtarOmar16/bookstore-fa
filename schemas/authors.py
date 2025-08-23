from pydantic import BaseModel, ConfigDict



class AuthorCreateSchema(BaseModel):
    name: str
    biography: str


class AuthorResponseSchema(BaseModel):
    model_config = ConfigDict(from_attributes=True)
    
    id: int
    name: str
    biography: str
