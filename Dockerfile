# Python 3.13 slim image
FROM python:3.13-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

WORKDIR /app

# System deps for psycopg/psycopg2, Pillow, and healthcheck
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    libpq-dev \
    curl \
 && rm -rf /var/lib/apt/lists/*

# Python deps (layer-cached)
COPY requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# App code
COPY . /app

# Railway will set $PORT; default 8000 for local
ENV PORT=8000
EXPOSE 8000

# Container healthcheck (matches our /healthz/ route)
HEALTHCHECK --interval=30s --timeout=10s --start-period=10s --retries=3 \
  CMD curl -fsS http://127.0.0.1:${PORT}/healthz/ || exit 1

# Start Gunicorn — change module if your project name differs
CMD ["gunicorn", "AdvancedWebDevelopment.wsgi:application", "--bind", "0.0.0.0:${PORT}", "--workers", "3", "--timeout", "30"]
