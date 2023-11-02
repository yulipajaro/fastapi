import os
from typing import Union

from fastapi import FastAPI
from starlette.responses import FileResponse

app = FastAPI()


@app.get("/")
def read_root():
    return {"Hello": "World"}


@app.get("/items/{item_id}")
def read_item(item_id: int, q: Union[str, None] = None):
    return {"item_id": item_id, "q": q}


@app.get("/example_dates")
def get_example_dates():
    return FileResponse('data/example_dates.json')


@app.get("/list_nit")
def get_list_nit():
    return FileResponse('data/list_nit.json')
