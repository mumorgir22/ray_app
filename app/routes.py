from fastapi import APIRouter

from app.auth.routes import router as auth_router
from app.blogs.routes import router as blogs_router
from app.users.routes import router as users_router

router = APIRouter()

router.include_router(users_router, prefix="/users", tags=["users"])
router.include_router(blogs_router, prefix="/blogs", tags=["blog"])
router.include_router(auth_router, prefix="/auth", tags=["auth"])
