from fastapi import FastAPI
from app.routers.user import user

app = FastAPI()

app.include_router(user.router)

if __name__ == "__main__":
    import uvicorn

    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)
