from pydantic_settings import BaseSettings



class PaginationSettings(BaseSettings):
    PAGE_SIZE: int = 10  



class Settings(PaginationSettings):
    
    class Config:
        env_file = ".env"