from sqlalchemy.ext.asyncio import AsyncSession
from sqlmodel import select
from app.models import User
from passlib.hash import bcrypt
from sqlalchemy.exc import SQLAlchemyError
from typing import Optional

# Hash a password
def hash_password(password: str) -> str:
    return bcrypt.hash(password)

# Verify a password
def verify_password(password: str, hashed_password: str) -> bool:
    return bcrypt.verify(password, hashed_password)

# Retrieve a user by ID
async def get_user_by_id(user_id: int, session: AsyncSession) -> Optional[User]:
    try:
        result = await session.execute(select(User).where(User.id == user_id))
        return result.scalar_one_or_none()  # Returns the first result or None
    except SQLAlchemyError as e:
        # Handle SQLAlchemy errors (e.g., database issues)
        print(f"Error retrieving user by ID {user_id}: {e}")
        return None

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
