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
<<<<<<< HEAD
    return FileResponse('data/example_dates.json')


@app.get("/list_nit")
def get_list_nit():
    return FileResponse('data/list_nit.json')
=======
    current_dir = os.path.dirname(os.path.realpath(__file__))
    file_path = os.path.join(current_dir, 'data', 'example_dates.json')
    return FileResponse(file_path)
>>>>>>> 219b7cf7e6ec245f328c8a664bdd47140000e8e0
