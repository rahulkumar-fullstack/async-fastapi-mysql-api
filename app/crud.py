from sqlalchemy.ext.asyncio import AsyncSession
from sqlmodel import select
from app.models import User
import bcrypt
from sqlalchemy.exc import SQLAlchemyError
from typing import Optional, List

# Hash a password
def hash_password(password: str) -> str:
    return bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')

# Verify a password
def verify_password(password: str, hashed_password: str) -> bool:
    return bcrypt.checkpw(password.encode('utf-8'), hashed_password.encode('utf-8'))

# Retrieve a user by ID
async def get_user_by_id(user_id: int, session: AsyncSession) -> Optional[User]:
    try:
        result = await session.execute(select(User).where(User.id == user_id))
        return result.scalar_one_or_none()  # Returns the first result or None
    except SQLAlchemyError as e:
        # Handle SQLAlchemy errors (e.g., database issues)
        print(f"Error retrieving user by ID {user_id}: {e}")
        return None

# Retrieve all users
async def get_all_users(session: AsyncSession) -> List[User]:
    try:
        result = await session.execute(select(User))
        return result.scalars().all()
    except SQLAlchemyError as e:
        print(f"Error retrieving all users: {e}")
        return []

# Create a new user
async def create_user(user: User, session: AsyncSession) -> Optional[User]:
    try:
        # Hash the password before saving
        user.password = hash_password(user.password)

        # Add the new user to the session and commit the transaction
        session.add(user)
        await session.commit()

        # Refresh the user object to load database-generated fields like ID
        await session.refresh(user)
        
        return user
    except SQLAlchemyError as e:
        # Rollback in case of an error and log the issue
        await session.rollback()
        print(f"Error creating user: {e}")
        return None

# Update a user
async def update_user(user_id: int, user_data: dict, session: AsyncSession) -> Optional[User]:
    try:
        result = await session.execute(select(User).where(User.id == user_id))
        user = result.scalar_one_or_none()
        if user:
            for key, value in user_data.items():
                if key == "password":
                    value = hash_password(value)
                setattr(user, key, value)
            await session.commit()
            await session.refresh(user)
        return user
    except SQLAlchemyError as e:
        await session.rollback()
        print(f"Error updating user {user_id}: {e}")
        return None

# Delete a user
async def delete_user(user_id: int, session: AsyncSession) -> bool:
    try:
        result = await session.execute(select(User).where(User.id == user_id))
        user = result.scalar_one_or_none()
        if user:
            await session.delete(user)
            await session.commit()
            return True
        return False
    except SQLAlchemyError as e:
        await session.rollback()
        print(f"Error deleting user {user_id}: {e}")
        return False
