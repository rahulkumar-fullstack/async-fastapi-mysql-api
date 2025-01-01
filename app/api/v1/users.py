from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession
from app.database import async_session
from app.models import User
from app.crud import create_user, get_user_by_id, update_user, delete_user

router = APIRouter()

# Dependency to get DB session
async def get_db():
    async with async_session() as session:
        yield session

# Create user endpoint
@router.post("/users/", response_model=User)
async def create_new_user(user: User, db: AsyncSession = Depends(get_db)):
   # Check if the user already exists
    existing_user = await get_user_by_id(user.id, db)
    if existing_user:
        raise HTTPException(status_code=400, detail="User already exists")
    
    # Create and return the new user
    created_user = await create_user(user, db)
    return created_user

# Get user endpoint
@router.get("/users/{user_id}", response_model=User)
async def read_user(user_id: int, db: AsyncSession = Depends(get_db)):
    user = await get_user_by_id(user_id, db)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user

# Update user endpoint
@router.put("/users/{user_id}", response_model=User)
async def update_existing_user(user_id: int, user: User, db: AsyncSession = Depends(get_db)):
    existing_user = await get_user_by_id(user_id, db)
    if not existing_user:
        raise HTTPException(status_code=404, detail="User not found")
    
    updated_user = await update_user(user_id, user, db)
    return updated_user

# Delete user endpoint
@router.delete("/users/{user_id}", response_model=User)
async def delete_existing_user(user_id: int, db: AsyncSession = Depends(get_db)):
    user = await get_user_by_id(user_id, db)
    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    
    await delete_user(user_id, db)
    return user
