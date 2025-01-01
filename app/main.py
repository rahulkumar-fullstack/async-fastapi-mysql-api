from fastapi import FastAPI
from app.database import init_db
from app.api.routes import router as api_router

# Define a lifespan context manager
async def lifespan(app: FastAPI):
    # Perform startup tasks
    print("Starting up...")
    await init_db()
    yield  # Yield control to FastAPI
    # Perform cleanup tasks (if any)
    print("Shutting down...")

# Initialize FastAPI app with title and lifespan
app = FastAPI(
    title="Async API with FastAPI and MySQL",  # Title of the application
    lifespan=lifespan  # Lifespan context manager for startup and shutdown
)

# Include API routes
app.include_router(api_router, prefix="/api", tags=["API"])
