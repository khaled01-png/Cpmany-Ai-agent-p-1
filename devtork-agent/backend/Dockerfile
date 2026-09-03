# DevTork AI Agent - Backend Dockerfile
#
# WHAT: Builds a container image for the FastAPI backend.
# WHY: So the backend runs identically on your machine and later on
#      any server, without "works on my machine" issues.

FROM python:3.11-slim

WORKDIR /app

# Install dependencies first (separate layer) so Docker can cache this
# step and skip reinstalling packages every time only app code changes.
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the backend source code
COPY . .

EXPOSE 8000

CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]
