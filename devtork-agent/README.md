# DevTork AI Agent

An AI employee for DevTork Studio — handles client chat, lead
qualification, requirement collection, and human handoff.

**Status:** Phase 1 (project setup) complete. See `docs/DEVELOPMENT_LOG.md`
for full build history.

## Stack
- Frontend: Next.js + TypeScript + Tailwind
- Backend: Python + FastAPI
- AI: Google Gemini API
- Database: PostgreSQL + pgvector
- Cache/Jobs: Redis
- Containerization: Docker

## Run locally (Docker — recommended)

1. Copy the environment template:
   ```
   cp .env.example .env
   ```
2. Start everything:
   ```
   docker compose up --build
   ```
3. Visit:
   - Frontend: http://localhost:3000
   - Backend docs (Swagger): http://localhost:8000/docs
   - Backend health check: http://localhost:8000/health

## Run backend without Docker (alternative)

```
cd backend
python -m venv venv
source venv/bin/activate    # Windows: venv\Scripts\activate
pip install -r requirements.txt
cp ../.env.example ../.env
uvicorn main:app --reload
```

## Run frontend without Docker (alternative)

```
cd frontend
npm install
npm run dev
```

## Project structure

```
devtork-agent/
├── frontend/        Next.js app (chat UI + admin dashboard)
├── backend/
│   ├── api/          FastAPI routes
│   ├── models/        SQLAlchemy models
│   ├── schemas/        Pydantic request/response schemas
│   ├── services/        business logic (scoring, notifications)
│   ├── agents/            AI agent orchestration
│   ├── tools/               agent tool functions
│   ├── rag/                   embeddings + retrieval
│   ├── database/                 DB connection/session
│   ├── auth/                       JWT auth
│   └── utils/                        config, shared helpers
├── docs/             Development log, tech map, agent docs
├── docker/
├── scripts/
├── docker-compose.yml
└── .env.example
```

## Documentation
- `docs/DEVELOPMENT_LOG.md` — full history of every build phase
- `docs/TECHNOLOGY_MAP.md` — every technology used, where, and its cost
- `docs/AGENT_WORKFLOW.md` — how a message flows through the agent
- `docs/AGENT_TOOLS.md` — every tool the AI can call
