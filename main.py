from fastapi import FastAPI
from fastapi.params import Query

from typing import Optional

from deta import Deta

app = FastAPI()

deta = Deta("c0u8ot8a_bSfeMUZF2gojqebYapDtACkPpi8ZBBQ8")

db = deta.Base("todos")

@app.get("/")
async def index():
    return "Hello, world!"

@app.get("/todos")
async def get_todos(completed: Optional[bool] = Query(None, description="is todo completed")):
    if completed is None:
        completed = False
    todos = db.fetch({"completed": completed})
    return todos

@app.post("/todos")
async def create_todo(todo: dict):
    return db.create(todo)

@app.put("/todos/{id}")
async def update_todo(id: int, todo: dict):
    return db.update(id, todo)

@app.delete("/todos/{id}")
async def delete_todo(id: int):
    return db.delete(id)
