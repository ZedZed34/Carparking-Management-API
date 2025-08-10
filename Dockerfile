# Use the official Python image as a base (latest stable with security patches)
FROM python:3.11.8-slim

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1
ENV DJANGO_SETTINGS_MODULE=AdvancedWebDevelopment.settings

# Set work directory
WORKDIR /app

# Install system dependencies
RUN apt-get update \
    && apt-get install -y --no-install-recommends \
        postgresql-client \
        build-essential \
        gcc \
        python3-dev \
        libpq-dev \
        curl \
    && rm -rf /var/lib/apt/lists/*

# Install Python dependencies
COPY requirements.txt /app/
RUN pip install --no-cache-dir --upgrade pip \
    && pip install --no-cache-dir -r requirements.txt \
    && pip install --no-cache-dir psycopg2-binary==2.9.9

# Copy project
COPY . /app/

# Create staticfiles directory
RUN mkdir -p /app/staticfiles

# Collect static files
RUN python manage.py collectstatic --noinput

# Create a non-root user (but run migrations as root first)
RUN adduser --disabled-password --gecos '' appuser

# Expose port
EXPOSE 8000

# Health check
HEALTHCHECK --interval=30s --timeout=30s --start-period=5s --retries=3 \
    CMD curl -f http://localhost:8000/health/ || exit 1

# Run the application (migrations first as root, then switch to appuser for gunicorn)
CMD ["sh", "-c", "python manage.py migrate && chown -R appuser:appuser /app && su appuser -c 'gunicorn --bind 0.0.0.0:${PORT:-8000} --workers 3 --worker-class sync --max-requests 1000 --max-requests-jitter 100 --timeout 30 AdvancedWebDevelopment.wsgi:application'"]
