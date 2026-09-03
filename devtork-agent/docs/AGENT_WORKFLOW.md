# DevTork AI Agent — Agent Workflow

**Status: Not yet implemented.** This document will be filled in during
Phase 5 (AI Agent + Tool Calling), once the agent orchestration logic
actually exists in `backend/agents/`.

## Planned flow (for reference — subject to refinement during Phase 5)

```
Client
  ↓
Chat UI (Next.js)
  ↓
FastAPI Backend (/api/chat)
  ↓
Conversation Memory (load history from PostgreSQL)
  ↓
Knowledge Retrieval (pgvector similarity search, if relevant)
  ↓
Gemini API (system prompt + history + retrieved context + available tools)
  ↓
Tool Selection (Gemini decides: reply directly, or call a tool)
  ↓
Tool Execution (backend runs the actual function, e.g. create_lead)
  ↓
Database / External API (the tool's real side effect)
  ↓
Tool Result (returned to Gemini)
  ↓
Gemini (produces final natural-language response)
  ↓
Final Response
  ↓
Client
```

Each stage above will be documented in detail — what data moves,
what code handles it, and why — once it is actually built in Phase 5
and Phase 6 (memory) and Phase 7 (knowledge retrieval).
