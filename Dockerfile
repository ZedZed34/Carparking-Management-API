# Use slim Python for smaller images
FROM python:3.12-slim

# Prevents Python from writing .pyc files and enables unbuffered logs
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

# System deps (psycopg2, Pillow, etc.)
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential libpq-dev curl \
 && rm -rf /var/lib/apt/lists/*

# Workdir
WORKDIR /app

# Install Python deps first for better layer caching
COPY requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy app
COPY . /app

# Gunicorn will bind to $PORT (Railway sets it). Default fallback 8000.
ENV PORT=8000
EXPOSE 8000

# Start Gunicorn (replace myproject.wsgi with your actual wsgi path)
CMD ["gunicorn", "myproject.wsgi:application", "--bind", "0.0.0.0:${PORT}", "--workers", "3"]
