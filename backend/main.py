from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import JSONResponse
import uvicorn
from typing import Dict, Any

# Import routers from modules
from src.auth.router import router as auth_router
from src.receipts.router import router as receipts_router
from src.inventory.router import router as inventory_router
from src.planning.router import router as planning_router
from src.analytics.router import router as analytics_router
from src.integrations.router import router as integrations_router

# Create FastAPI application
app = FastAPI(
    title="Receipt-to-Meal Planner API",
    description="Backend API for converting grocery receipts into personalized meal plans",
    version="1.0.0",
    docs_url="/docs",
    redoc_url="/redoc"
)

# CORS middleware configuration
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # In production, replace with specific origins
    allow_credentials=True,
    allow_methods=["GET", "POST", "PUT", "DELETE", "PATCH"],
    allow_headers=["*"],
)

# Health check endpoint
@app.get("/health")
async def health_check() -> JSONResponse:
    """Health check endpoint for monitoring"""
    return JSONResponse(
        status_code=200,
        content={
            "status": "healthy",
            "service": "receipt-meal-planner-api",
            "version": "1.0.0"
        }
    )

# Root endpoint
@app.get("/")
async def root() -> Dict[str, str]:
    """Root endpoint with API information"""
    return {
        "message": "Welcome to Receipt-to-Meal Planner API",
        "documentation": "/docs",
        "health": "/health",
        "version": "1.0.0"
    }

# Include module routers
app.include_router(auth_router, prefix="/api/v1/auth", tags=["Authentication"])
app.include_router(receipts_router, prefix="/api/v1/receipts", tags=["Receipts"])
app.include_router(inventory_router, prefix="/api/v1/inventory", tags=["Inventory"])
app.include_router(planning_router, prefix="/api/v1/planning", tags=["Meal Planning"])
app.include_router(analytics_router, prefix="/api/v1/analytics", tags=["Analytics"])
app.include_router(integrations_router, prefix="/api/v1/integrations", tags=["Integrations"])

# Global exception handler
@app.exception_handler(Exception)
async def global_exception_handler(request, exc):
    """Global exception handler for unhandled errors"""
    return JSONResponse(
        status_code=500,
        content={
            "detail": "Internal server error",
            "message": "An unexpected error occurred"
        }
    )

if __name__ == "__main__":
    uvicorn.run(
        "main:app",
        host="0.0.0.0",
        port=8000,
        reload=True,
        log_level="info"
    )
