from fastapi import APIRouter, HTTPException
from app.schemas import TaskCreate , TaskRead, TaskUpdate, TaskPatch, TaskDelete

router = APIRouter(prefix="/tasks", tags=["tasks"])
Todos: list[dict] = []
NEXT_ID = 1
TASK_COMPLETED: bool = False


@router.post('', response_model=TaskCreate, status_code=201)
def create_task(payload: TaskCreate):
    global NEXT_ID

    todo = {
        "id": NEXT_ID,
        "title": payload.title,
        "description": payload.description,
       "completed": TASK_COMPLETED
    }

    NEXT_ID += 1
    Todos.append(todo)

    return todo

@router.get("", response_model=list[TaskRead], status_code=200)
def list_todos():
    if Todos.__len__() == 0:
        raise HTTPException(status_code=204, detail="No content")
    return Todos

##@router.get("?search={word}", response_model=list[TaskRead], status_code=200)
#def search_todos(word: str):
 #   result = []
 #   for s in Todos:
     #   if word in s['title'] or word in s['description']:
      #      result.append(s)
 #   if result.__len__() == 0:
     #   raise HTTPException(status_code=204, detail="No content")
 #   return result

@router.get("/{task_id}", response_model=TaskRead)
def get_task(task_id: int):
    for s in Todos:
        if s['id'] == task_id:
            return s
    raise HTTPException(status_code=404, detail="la tâche n'existe pas")

@router.put("/{task_id}", response_model=TaskUpdate, status_code=200)
def update_task(task_id: int, payload: TaskUpdate):
    for s in Todos:
        if s['id'] == task_id:
            s['title'] = payload.title
            s['description'] = payload.description
            #s['completed'] = payload.completed
            return s
    raise HTTPException(status_code=404, detail="la tâche n'existe pas")

@router.delete("/{task_id}", response_model=TaskDelete,status_code=200)
def delete_task(task_id: int):
    for s in Todos:
        if s['id'] == task_id:
            Todos.remove(s)
            return {"id": task_id}
    raise HTTPException(status_code=404, detail="la tâche n'existe pas")

@router.patch("/{task_id}", response_model=TaskPatch)
def patch_task(task_id: int, payload: TaskPatch):
    for s in Todos:
        if s['id'] == task_id:
            s['title'] = payload.title
            s['description'] = payload.description
            #s['completed'] = payload.completed
            return s
    raise HTTPException(status_code=404, detail="la tâche n'existe pas")

#@router.put("/{task_id}/complete", response_model=TaskRead, status_code=200)
#def complete_student(task_id: int):
    #for s in Todos:
     #if s['id'] == task_id:
     #     s['completed'] = True
    #return s
#raise HTTPException(status_code=404, detail="la tâche n'existe pas")
