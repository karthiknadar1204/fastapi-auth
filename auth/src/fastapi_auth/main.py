from fastapi import FastAPI
import uvicorn
from fastapi_auth.utils.init_db import create_tables

app = FastAPI()

@app.get("/")
def health_check():
    return {"message": "Hello, World!"}

def start():
    """Start the FastAPI server."""
    create_tables()
    uvicorn.run("fastapi_auth.main:app", host="127.0.0.1", port=8080, reload=True)

if __name__ == "__main__":
    start()