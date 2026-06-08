from fastapi import FastAPI
from app.core.config import settings
from app.db.database import engine
from app.db.database import Base

from app.db import models
from app.api.v1.auth import router as auth_router
from app.api.v1.products import router as products_router

Base.metadata.create_all(bind=engine)

print(settings.DATABASE_URL)

app = FastAPI(
    title="Backend Intern Assignment API",
    version="1.0.0"
)

app.include_router(
    auth_router,
    prefix="/api/v1/auth",
    tags=["Authentication"]
)

app.include_router(
    products_router,
    prefix="/api/v1/products",
    tags=["Products"]
)


@app.get("/")
def root():
    return {
        "message": "Backend API is running"
    }
