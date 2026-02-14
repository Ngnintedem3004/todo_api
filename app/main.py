from fastapi import FastAPI
from app.routers.tasks_db import router as tasks_router
from database import Base 

app = FastAPI(title="Todo API", description="A simple Todo API built with FastAPI", version="1.1.0")
app.include_router(tasks_router) 
print("Création de la base de données...")
#Base.metadata.create_all(bind=engine)
print("Fait ! Regardez si le fichier todos.db est apparu.")
@app.get('/')
def home():
    return {"message": "Api is running"}
