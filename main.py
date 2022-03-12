from fastapi import FastAPI
from fastapi.params import Query

from typing import Optional


app = FastAPI()


@app.get("/")
async def index():
    return "Hello, world!"
