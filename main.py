from fastapi import FastAPI

app = FastAPI()

print('hello')


@app.post('/get_routes')
async def get_routes(log: str):
    print(log)
