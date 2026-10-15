from fastapi import FastAPI
from src.core.router import router

app = FastAPI(
    title="Lab3 FastAPI Project",
    description="Lab project with FastAPI and Swagger UI",
    version="0.1.0",
)

app.include_router(router)