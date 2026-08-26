from fastapi import FastAPI

app = FastAPI()

@app.get("/todo/{id}")
async def users(id: int):
    return {"id": 1, "title": "Estudar", "description": "Matemática", "date": "2026-08-30 04:05:06", "done": False}
