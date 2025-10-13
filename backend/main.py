import uvicorn
from fastapi import FastAPI
from routers import user
from database import get_db, create_tables

app = FastAPI()

app.include_router(user.router)

@app.on_event("startup")
def startup_event():
    create_tables()
    

if __name__ == "__main__":
    uvicorn.run("main:app",
                host="0.0.0.0",
                port=8000,
                reload=True)
