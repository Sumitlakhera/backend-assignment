from fastapi import FastAPI
from app.core.config import settings

print(settings.DATABASE_URL)

app = FastAPI(
    title="Backend Intern Assignment API",
    version="1.0.0"
)


@app.get("/")
def root():
    return {
        "message": "Backend API is running"
    }
