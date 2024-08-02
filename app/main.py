from fastapi import FastAPI

app = FastAPI()


@app.post('/get_routes')
async def get_routes(log: str):
    print(log)
