from fastapi import FastAPI
from app.routers.tasks import router as tasks_router

app = FastAPI(title="Todo API", description="A simple Todo API built with FastAPI", version="1.0.0")
app.include_router(tasks_router) 
@app.get('/')
def home():
    return {"message": "Api is running"}
