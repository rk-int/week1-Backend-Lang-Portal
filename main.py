import os
from fastapi import FastAPI
from app.database import engine, Base, get_db
from app.routes import words, groups, sessions, reviews

# Initialize the FastAPI app
app = FastAPI(title="Lang Portal API")

# Create database tables
Base.metadata.create_all(bind=engine)

# Include routers
app.include_router(words.router, prefix="/words", tags=["Words"])
app.include_router(groups.router, prefix="/groups", tags=["Groups"])
app.include_router(sessions.router, prefix="/study_sessions", tags=["Study Sessions"])
app.include_router(reviews.router, prefix="/reviews", tags=["Word Reviews"])

# Dependency Injection for DB session
@app.middleware("http")
async def db_session_middleware(request: Request, call_next):
    response = Response("Internal server error", status_code=500)
    try:
        request.state.db = next(get_db())
        response = await call_next(request)
    finally:
        request.state.db.close()
    return response

# Root endpoint
@app.get("/")
def root():
    return {"message": "Welcome to Lang Portal API"}

