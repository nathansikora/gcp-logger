from typing import Dict
from fastapi import FastAPI

app = FastAPI()


@app.post('/')
async def get_routes(data: Dict):
    log = data.get('msg', None)
    if log is not None:
        print(log)
    else:
        print('kaka')
        print(f'{data}')
    return 200


@app.get("/")
def read_root():
    return {"Hello": "World"}