from fastapi import APIRouter, HTTPException
from fastapi.params import Depends
from app.schemas import TaskCreate , TaskRead, TaskUpdate, TaskPatch, TaskDelete
from models import Todo
from sqlalchemy.orm import Session

from database import get_db

router = APIRouter(prefix="/tasks", tags=["tasks(DB)"])
Todos: list[dict] = []
NEXT_ID = 1
TASK_COMPLETED: bool = False


@router.post('', response_model=TaskCreate, status_code=201)
def create_task(payload: TaskCreate , db: Session = Depends(get_db)):

    todo = Todo(
        title=payload.title,
        description=payload.description,
    )
    db.add(todo)
    db.commit()
    db.refresh(todo)
    return todo

@router.get("", response_model=list[TaskRead], status_code=200)
def list_todos( db: Session = Depends(get_db)):
    if Todos.__len__() == 0:
        raise HTTPException(status_code=204, detail="No content")
    return db.query(Todo).order_by(Todo.id.asc()).all()

@router.get("/{task_id}", response_model=TaskRead)
def get_task(task_id: int , db: Session = Depends(get_db)):
    task = db.query(Todo).filter(Todo.id == task_id).first()
    if task is None:
        raise HTTPException(status_code=404, detail="la tâche n'existe pas")
    return task

@router.put("/{task_id}", response_model=TaskUpdate, status_code=200)
def update_task(task_id: int, payload: TaskUpdate, db: Session = Depends(get_db)):
    task = db.query(Todo).filter(Todo.id == task_id).first()
    if task is None:
        raise HTTPException(status_code=404, detail="la tâche n'existe pas")
    task.title = payload.title
    task.description = payload.description
    #task.completed = payload.completed
    db.commit()
    db.refresh(task)
    return task

@router.delete("/{task_id}", response_model=TaskDelete,status_code=200)
def delete_task(task_id: int, db: Session = Depends(get_db)):
    task = db.query(Todo).filter(Todo.id == task_id).first()
    if task is None:
        raise HTTPException(status_code=404, detail="la tâche n'existe pas")
    db.delete(task)
    db.commit()
    return {"id": task_id}

@router.patch("/{task_id}", response_model=TaskPatch)
def patch_task(task_id: int, payload: TaskPatch, db: Session = Depends(get_db)):
    task = db.query(Todo).filter(Todo.id == task_id).first()
    if task is None:
        raise HTTPException(status_code=404, detail="la tâche n'existe pas")
    task.title = payload.title
    task.description = payload.description
    #task.completed = payload.completed
    db.commit()
    db.refresh(task)
    return task
