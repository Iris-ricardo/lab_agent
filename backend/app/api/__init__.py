from fastapi import APIRouter
from app.api.auth import router as auth_router
from app.api.user import router as user_router

api = APIRouter(prefix="/api")

api.include_router(router=auth.router)
api.include_router(router=user.router)

