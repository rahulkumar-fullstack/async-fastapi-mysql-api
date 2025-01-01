from sqlmodel import SQLModel, Field

# User model
class User(SQLModel, table=True):
    id: int = Field(default=None, primary_key=True)
    name: str
    email: str
    password: str

