/*
  DevTork AI Agent - Frontend Placeholder Page

  WHAT THIS IS (Phase 1):
  A minimal page that just confirms the Next.js app runs and can
  reach the FastAPI backend's /health endpoint. This is NOT the
  real chat UI -- that is built in Phase 10, once the AI agent
  actually exists on the backend (Phases 4-9).

  WHY WE START THIS SMALL:
  Building a chat interface before there's an agent to talk to
  would just be a fake UI with nothing real behind it -- which the
  project rules explicitly say to avoid.
*/

"use client";

import { useEffect, useState } from "react";

export default function Home() {
  const [backendStatus, setBackendStatus] = useState<string>("checking...");

  useEffect(() => {
    fetch("http://localhost:8000/health")
      .then((res) => res.json())
      .then((data) => setBackendStatus(data.status))
      .catch(() => setBackendStatus("unreachable"));
  }, []);

  return (
    <main style={{ padding: "2rem", fontFamily: "sans-serif" }}>
      <h1>DevTork AI Agent</h1>
      <p>Phase 1: Project setup</p>
      <p>Backend status: <strong>{backendStatus}</strong></p>
    </main>
  );
}
