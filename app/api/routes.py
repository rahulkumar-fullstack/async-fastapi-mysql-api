from fastapi import APIRouter
from app.api.v1 import users

# Create a main router
router = APIRouter()

# Include versioned routers
router.include_router(users.router, prefix="/v1/users", tags=["Users"])

