# DevTork AI Agent — Development Log

This file is the complete history of how the DevTork AI Agent was built.
Every phase adds an entry below. Nothing is removed.

---

## Phase 1 — Project Setup + Architecture

**Date:** 2026-09-01

**Feature built:**
Base project skeleton: folder structure, Docker orchestration for all
planned services, FastAPI "hello world" + health check, minimal Next.js
placeholder page, environment variable template, documentation system.

**Technologies used:**
- FastAPI (backend web framework)
- Uvicorn (ASGI server that runs FastAPI)
- pydantic-settings (environment variable loading/validation)
- Next.js 14 + React + TypeScript (frontend)
- Docker + Docker Compose (containerization/orchestration)
- PostgreSQL via `pgvector/pgvector:pg16` image (database, vector-ready)
- Redis (defined in infra, not wired into code yet)

**Libraries installed (backend):**
- fastapi==0.115.0
- uvicorn[standard]==0.32.0
- pydantic==2.9.2
- pydantic-settings==2.6.0

**Libraries installed (frontend):**
- next, react, react-dom
- typescript, @types/react, @types/node
- tailwindcss, postcss, autoprefixer (configured but not yet styling anything real)

**Files created:**
- `backend/main.py` — FastAPI app entrypoint, CORS, `/` and `/health`
- `backend/utils/config.py` — centralized settings loader
- `backend/requirements.txt`
- `backend/Dockerfile`
- `backend/{api,models,schemas,services,agents,tools,rag,database,auth,utils}/__init__.py` — empty package placeholders for future phases
- `frontend/app/page.tsx` — placeholder page that pings backend `/health`
- `frontend/app/layout.tsx`
- `frontend/package.json`
- `frontend/tsconfig.json`
- `frontend/Dockerfile`
- `docker-compose.yml` — backend, frontend, db (pgvector), redis
- `.env.example`
- `.gitignore`
- `docs/DEVELOPMENT_LOG.md` (this file)
- `docs/TECHNOLOGY_MAP.md`
- `docs/AGENT_WORKFLOW.md`
- `docs/AGENT_TOOLS.md`
- `README.md`

**Files modified:** None (first phase).

**APIs integrated:** None yet. Gemini API arrives in Phase 4.

**Database changes:** None yet. `db` container is defined and running,
but no tables exist until Phase 2.

**Important decisions:**
- Chose Google Gemini API over OpenAI for the AI Brain, based on the
  team's budget constraints (generous free tier). LLM calls are
  isolated behind a service abstraction (built in Phase 4) so the
  provider can be swapped later with a config change, not a rewrite.
- Chose pgvector over a separate vector database (Pinecone/Weaviate)
  to avoid running/paying for an extra service.
- CORS is restricted to the known frontend origin rather than "*",
  since this API will eventually handle real client PII.

**Testing performed:**
- Backend health check reachable at `/health`.
- Frontend placeholder page successfully calls backend `/health` and
  displays the status.
- `docker compose up` brings up all four services without errors.

**Current status:** Phase 1 complete. No AI, database tables, or real
business logic exists yet — this phase is infrastructure only.

**Next step:** Phase 2 — Database + Models (users, leads, clients,
conversations, messages, knowledge_documents, knowledge_chunks,
notifications, agent_logs).
