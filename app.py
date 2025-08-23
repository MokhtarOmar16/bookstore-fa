from fastapi import FastAPI , APIRouter
from fastapi.staticfiles import StaticFiles
from routers import books, authors

app = FastAPI()


app.mount("/static", StaticFiles(directory="static"), name="static")


api_router = APIRouter(prefix="/api")



api_router.include_router(books.router)
api_router.include_router(authors.router)


app.include_router(api_router)


if __name__ == "__main__":
    import uvicorn
    
    uvicorn.run("app:app", reload=True)