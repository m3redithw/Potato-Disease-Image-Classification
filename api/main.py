from fastapi import fastApi
import uvicorn

app = FastAPI()

@app.get('/ping')

async def ping():
    return "Hello, I am alibe"

if __name__ == '__main__':
    uvicorn.run(app, host = 'localhost', port =8000)