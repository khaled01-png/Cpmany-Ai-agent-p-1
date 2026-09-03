"""
DevTork AI Agent - Backend Entrypoint

WHAT THIS FILE DOES (Phase 1):
Creates the FastAPI application, enables CORS so the Next.js frontend
can talk to it, and exposes a health-check endpoint.

WHY IT MATTERS:
This is the "front door" of the whole backend. Every request from the
chat UI or admin dashboard eventually flows through this app object.
In later phases, we will `include_router(...)` here for:
  - /api/auth      (Phase 3)
  - /api/chat      (Phase 5)
  - /api/leads     (Phase 8)
  - /api/knowledge (Phase 7)
  - /api/dashboard (Phase 11)
  - /api/notifications (Phase 12)

We are NOT adding those yet -- Phase 1 is intentionally just the
skeleton, so you can run it and see a working server before any
real logic exists.

HOW TO RUN:
    cd backend
    uvicorn main:app --reload

Then visit http://localhost:8000/docs for the auto-generated
Swagger UI (this comes free from FastAPI, no extra library needed).
"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from utils.config import settings

app = FastAPI(
    title=settings.APP_NAME,
    description="AI Agent backend for DevTork Studio",
    version="0.1.0",
)

# CORS: without this, the browser blocks requests from the Next.js
# frontend (different port = different "origin") for security reasons.
# We explicitly allow only our own frontend origin, not "*", because
# an open CORS policy on an API that will later handle client PII
# (leads, emails, phone numbers) is a real security risk.
app.add_middleware(
    CORSMiddleware,
    allow_origins=[settings.FRONTEND_ORIGIN],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get("/")
def root():
    """Basic landing response so hitting the root URL isn't a 404."""
    return {
        "service": settings.APP_NAME,
        "status": "running",
        "phase": "1 - project setup",
    }


@app.get("/health")
def health_check():
    """
    Health check endpoint.

    WHY WE NEED THIS:
    Docker, deployment platforms, and monitoring tools (and n8n later,
    for automation triggers) commonly poll a /health endpoint to
    confirm the service is alive before routing traffic to it.
    """
    return {"status": "ok"}
