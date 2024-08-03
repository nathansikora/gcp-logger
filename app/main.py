from typing import Dict
from fastapi import FastAPI

app = FastAPI()


@app.post('/')
async def log(data: Dict):
    log = data.get('msg', None)
    if log is not None:
        print(log)
    return 200


@app.get("/")
def alive():
    return 200
