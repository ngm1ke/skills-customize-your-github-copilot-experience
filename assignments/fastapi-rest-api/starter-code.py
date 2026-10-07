from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI(title="Task Tracker API")

tasks = [
    {"id": 1, "title": "Review loops", "completed": False},
    {"id": 2, "title": "Practice functions", "completed": False},
]


class TaskCreate(BaseModel):
    title: str


@app.get("/tasks")
def list_tasks():
    # TODO: Return all tasks.
    pass


@app.get("/tasks/{task_id}")
def get_task(task_id: int):
    # TODO: Find and return the task, or raise HTTPException with status 404.
    pass


@app.post("/tasks", status_code=201)
def create_task(task: TaskCreate):
    # TODO: Create a task with a unique ID and completed set to False.
    # Append it to tasks and return it.
    pass
