import uvicorn
from fastapi import FastAPI
from routers import user

app = FastAPI()

app.include_router(user.router)

def main():
    print("Hello from backend!")


if __name__ == "__main__":
    uvicorn.run("main:app",
                host="0.0.0.0",
                port=8000,
                reload=True)
