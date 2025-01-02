from fastapi import FastAPI  # Import FastAPI framework

# Initialize FastAPI app instance
app = FastAPI()

# Import API routes from api module
from .api import router as api_router

# Include API router in the main app
app.include_router(api_router)
