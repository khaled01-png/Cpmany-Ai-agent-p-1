"""
DevTork AI Agent - Application Configuration

WHAT THIS FILE DOES:
Loads all configuration (API keys, DB URL, secrets) from environment
variables using pydantic-settings. Nothing is ever hardcoded here.

WHY THIS PATTERN:
- Keeps secrets out of source code (security requirement from spec).
- Gives us auto-validation: if a required env var is missing, the
  app fails fast at startup with a clear error, instead of failing
  later in a confusing way.
- One single place ("Settings") that every other file imports from,
  instead of scattering os.getenv() calls everywhere.

This file currently only defines the settings needed for Phase 1
(basic server config). Fields for the database, Gemini API, JWT
secret, etc. will be ADDED in Phase 2, 3, 4 respectively -- not
invented ahead of time, so you can see exactly when each one enters
the project.
"""

from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    # --- General app info ---
    APP_NAME: str = "DevTork AI Agent"
    APP_ENV: str = "development"  # development | production
    DEBUG: bool = True

    # --- Server ---
    BACKEND_HOST: str = "0.0.0.0"
    BACKEND_PORT: int = 8000

    # --- CORS (which frontend origins may call this API) ---
    FRONTEND_ORIGIN: str = "http://localhost:3000"

    model_config = SettingsConfigDict(
        env_file=".env",
        env_file_encoding="utf-8",
        extra="ignore",  # ignore unrelated env vars instead of crashing
    )


# Single shared instance imported across the whole backend
settings = Settings()
