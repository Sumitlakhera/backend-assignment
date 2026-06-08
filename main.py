from fastapi import FastAPI
from app.core.config import settings
from app.db.database import engine
from app.db.database import Base

from app.db import models

Base.metadata.create_all(bind=engine)

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
