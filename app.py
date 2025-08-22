from fastapi import FastAPI 
from fastapi.staticfiles import StaticFiles


app = FastAPI()


app.mount("/static", StaticFiles(directory="static"), name="static")


if __name__ == "__main__":
    import uvicorn
    
    uvicorn.run("app:app", reload=True)