# DevTork AI Agent — Technology Map

Updated every time a new technology is introduced. Nothing is added to
the project without first appearing in this table.

| Component | Technology | Purpose | Where Used | Cost |
|---|---|---|---|---|
| Backend framework | FastAPI | API server | `backend/main.py` | Free / Open Source |
| ASGI server | Uvicorn | Runs the FastAPI app | `backend/Dockerfile` | Free / Open Source |
| Config management | pydantic-settings | Load env vars safely | `backend/utils/config.py` | Free / Open Source |
| Frontend framework | Next.js | Chat UI + Admin dashboard | `frontend/` | Free / Open Source |
| Frontend language | TypeScript | Type-safe frontend code | `frontend/` | Free / Open Source |
| Styling | Tailwind CSS | UI styling | `frontend/` (configured, not yet used) | Free / Open Source |
| Database | PostgreSQL | Store all business data | `docker-compose.yml` (`db` service) | Free (self-hosted) |
| Vector search | pgvector | RAG / knowledge base similarity search | `db` service (Postgres extension) | Free / Open Source |
| Cache / background jobs | Redis | Defined for future async jobs | `docker-compose.yml` (`redis` service, not wired yet) | Free / Open Source |
| Containerization | Docker + Docker Compose | Run entire stack consistently | `docker-compose.yml`, `Dockerfile`s | Free / Open Source |
| AI Brain *(Phase 4)* | Google Gemini API | AI reasoning + tool calling | `backend/agents/` (not yet built) | Free tier (usage limits apply) |

**Not yet introduced (will appear here when built):**
SQLAlchemy (Phase 2, DB ORM), Alembic (Phase 2, migrations), JWT library
(Phase 3, auth), Gemini SDK (Phase 4), embedding model (Phase 7), n8n
(automation, later phase), SMTP/webhook client (Phase 12).
