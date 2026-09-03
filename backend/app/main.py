from fastapi import FastAPI
from routers import todo
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Permite que o Locust (porta 8089) acesse a API sem bloqueios de CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Ou adicione "http://localhost:8089" e "http://127.0.0.1:8089"
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(todo.router)