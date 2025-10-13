import uvicorn
from fastapi import FastAPI
from database import get_db, create_tables

app = FastAPI()

@app.get('/')
def main():
    return "home"

@app.on_event("startup")
def startup_event():
    create_tables()
    

if __name__ == "__main__":
    uvicorn.run("main:app",
                host="127.0.0.1",
                port=8000,
                reload=True)
