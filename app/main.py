from fastapi import FastAPI

app = FastAPI()

@app.get("/")
async def root():
    return {"message": "Hello World"}
    
# use connection pooling for database connections
# use connection pooling for database connections