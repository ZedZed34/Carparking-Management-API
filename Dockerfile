# Python 3.13 slim image
FROM python:3.13

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
# Give app more time to boot on cold start
HEALTHCHECK --interval=30s --timeout=10s --start-period=30s --retries=5 \
  CMD curl -fsS http://127.0.0.1:${PORT}/healthz/ || exit 1

# Start script with proper error handling
CMD ["sh", "-c", "python manage.py migrate && python manage.py collectstatic --noinput && (python scripts/load_and_store.py || echo 'Data loading failed, continuing...') && gunicorn AdvancedWebDevelopment.wsgi:application --bind 0.0.0.0:$PORT --workers 2 --timeout 60 --access-logfile - --error-logfile -"]
