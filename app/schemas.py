from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

class TaskCreate(BaseModel):
    title: str = Field(..., description="The title of the task" ,max_length=50)
    description: str = Field(..., description="The description of the task", max_length=255)
    #completed: bool = False

class TaskRead(BaseModel):
    id: int
    title: str
    description: str
    #completed: bool

class TaskUpdate(BaseModel):
    id: int = Field(..., description="The id of the task to update")
    title: str  = Field(..., description="The title of the task", max_length=50)
    description: str  = Field(...,description="The description of the task", max_length=255)
    #completed: bool  = Field(..., description="Whether the task is completed or not")

class TaskPatch(BaseModel):
    id: int = Field(..., description="The id of the task to update")
    title: str  = Field(..., description="The title of the task",max_length=50)
    description: str = Field(..., description="The description of the task",max_length=255)
    #completed: bool  = Field(..., description="Whether the task is completed or not")
    
class TaskDelete(BaseModel):
    id: int = Field(..., description="The id of the task to delete")