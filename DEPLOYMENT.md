# 🚀 Deployment Guide

This guide provides step-by-step instructions for deploying the Carpark Management API to various platforms.

## 📋 Prerequisites

- Git repository with the latest code
- Docker installed (for containerized deployment)
- Railway account (for Railway deployment)
- GitHub account (for CI/CD)

## 🚂 Railway Deployment

### Method 1: Automatic Deployment (Recommended)

1. **Prepare Repository**
   ```bash
   # Clone the repository
   git clone https://github.com/ZedZed34/Carparking-Management-API.git
   cd Carparking-Management-API
   
   # Push to your own GitHub repository
   git remote set-url origin https://github.com/YOUR_USERNAME/Carparking-Management-API.git
   git push -u origin main
   ```

2. **Connect to Railway**
   - Visit [Railway](https://railway.app)
   - Sign in with your GitHub account
   - Click "New Project"
   - Select "Deploy from GitHub repo"
   - Choose your repository

3. **Configure Environment Variables**
   In Railway dashboard, go to Variables tab and add:
   ```
   SECRET_KEY=your-super-secret-key-change-this-in-production
   DEBUG=False
   ALLOWED_HOSTS=*.railway.app
   ```

4. **Add PostgreSQL Database**
   - In your Railway project, click "New Service"
   - Select "PostgreSQL"
   - Railway will automatically set the `DATABASE_URL` environment variable

5. **Deploy**
   - Railway will automatically build and deploy your application
   - The deployment will be triggered on every push to the main branch

### Method 2: CLI Deployment

1. **Install Railway CLI**
   ```bash
   # Install Railway CLI
   curl -fsSL https://railway.app/install.sh | sh
   
   # Or with npm
   npm install -g @railway/cli
   ```

2. **Login and Deploy**
   ```bash
   # Login to Railway
   railway login
   
   # Initialize project
   railway init
   
   # Add PostgreSQL service
   railway add postgresql
   
   # Set environment variables
   railway variables set SECRET_KEY="your-secret-key"
   railway variables set DEBUG=False
   railway variables set ALLOWED_HOSTS="*.railway.app"
   
   # Deploy
   railway up
   ```

3. **Post-deployment**
   ```bash
   # Run migrations
   railway run python manage.py migrate
   
   # Load initial data
   railway run python scripts/load_and_store.py
   ```

## 🐳 Docker Deployment

### Local Development

1. **Build and Run with Docker Compose**
   ```bash
   # Clone repository
   git clone https://github.com/ZedZed34/Carparking-Management-API.git
   cd Carparking-Management-API
   
   # Start all services
   docker-compose up --build
   
   # Run in background
   docker-compose up -d
   
   # View logs
   docker-compose logs -f web
   ```

2. **Access Application**
   - Web UI: http://localhost
   - API: http://localhost/api/v1/carparks/
   - Admin: http://localhost/admin/

### Production Docker

1. **Build Production Image**
   ```bash
   # Build image
   docker build -t carpark-api:latest .
   
   # Run with environment variables
   docker run -d \
     --name carpark-api \
     -p 8000:8000 \
     -e SECRET_KEY="your-secret-key" \
     -e DEBUG=False \
     -e DATABASE_URL="postgresql://user:password@host:port/dbname" \
     -e ALLOWED_HOSTS="yourdomain.com" \
     carpark-api:latest
   ```

2. **Using Docker Compose for Production**
   ```yaml
   # docker-compose.prod.yml
   version: '3.8'
   services:
     web:
       image: carpark-api:latest
       ports:
         - "8000:8000"
       environment:
         - SECRET_KEY=${SECRET_KEY}
         - DEBUG=False
         - DATABASE_URL=${DATABASE_URL}
         - ALLOWED_HOSTS=${ALLOWED_HOSTS}
   ```

## ☁️ Other Cloud Platforms

### Heroku

1. **Prepare for Heroku**
   ```bash
   # Install Heroku CLI
   # Add Procfile (already included in project)
   echo "web: gunicorn AdvancedWebDevelopment.wsgi:application" > Procfile
   ```

2. **Deploy to Heroku**
   ```bash
   # Login and create app
   heroku login
   heroku create your-carpark-api
   
   # Add PostgreSQL
   heroku addons:create heroku-postgresql:mini
   
   # Set environment variables
   heroku config:set SECRET_KEY="your-secret-key"
   heroku config:set DEBUG=False
   heroku config:set ALLOWED_HOSTS="your-carpark-api.herokuapp.com"
   
   # Deploy
   git push heroku main
   
   # Run migrations
   heroku run python manage.py migrate
   heroku run python scripts/load_and_store.py
   ```

### DigitalOcean App Platform

1. **Create App Spec**
   ```yaml
   # app.yaml
   name: carpark-api
   services:
   - name: web
     source_dir: /
     github:
       repo: YOUR_USERNAME/Carparking-Management-API
       branch: main
     run_command: gunicorn --worker-tmp-dir /dev/shm AdvancedWebDevelopment.wsgi:application
     environment_slug: python
     instance_count: 1
     instance_size_slug: basic-xxs
     envs:
     - key: SECRET_KEY
       value: your-secret-key
     - key: DEBUG
       value: "False"
   databases:
   - name: db
     engine: PG
     version: "13"
   ```

2. **Deploy**
   ```bash
   # Install doctl CLI
   doctl apps create --spec app.yaml
   ```

## 🔧 Environment Variables Reference

### Required Variables

| Variable | Description | Example |
|----------|-------------|---------|
| `SECRET_KEY` | Django secret key | `django-insecure-xyz...` |
| `DEBUG` | Debug mode | `False` |
| `ALLOWED_HOSTS` | Allowed hostnames | `*.railway.app,yourdomain.com` |

### Optional Variables

| Variable | Description | Default | Example |
|----------|-------------|---------|---------|
| `DATABASE_URL` | Database connection string | SQLite | `postgresql://user:pass@host:5432/db` |
| `PORT` | Application port | `8000` | `8000` |
| `DJANGO_SETTINGS_MODULE` | Settings module | `AdvancedWebDevelopment.settings` | Same |

### Security Variables (Production)

| Variable | Description | Default |
|----------|-------------|---------|
| `SECURE_SSL_REDIRECT` | Force HTTPS | `True` |
| `SECURE_PROXY_SSL_HEADER` | SSL header | `HTTP_X_FORWARDED_PROTO,https` |

## 🔄 CI/CD Setup

### GitHub Actions

The repository includes pre-configured workflows:

1. **Test Pipeline** (`.github/workflows/test.yml`)
   - Runs on pull requests and develop branch
   - Multi-version Python testing
   - Code quality checks
   - Security scanning

2. **Deployment Pipeline** (`.github/workflows/deploy.yml`)
   - Runs on main branch pushes
   - Builds and pushes Docker images
   - Deploys to Railway
   - Post-deployment tasks

### Required Secrets

Add these secrets in GitHub repository settings:

```
DOCKER_USERNAME=your-dockerhub-username
DOCKER_PASSWORD=your-dockerhub-password-or-token
RAILWAY_TOKEN=your-railway-project-token
```

### Getting Railway Token

1. Go to [Railway](https://railway.app)
2. Navigate to your project
3. Go to Settings → Tokens
4. Generate a new deployment token
5. Copy the token to GitHub secrets

## 🔍 Health Checks & Monitoring

### Application Health

```bash
# Check API health
curl https://your-app.railway.app/api/v1/carparks/

# Check specific endpoint
curl https://your-app.railway.app/api/v1/carparks/types/
```

### Database Health

```bash
# Connect to Railway database
railway connect postgresql

# Check tables
\dt

# Check data
SELECT COUNT(*) FROM carparks_carpark;
```

### Logs

```bash
# Railway logs
railway logs

# Docker logs
docker-compose logs -f web

# Heroku logs
heroku logs --tail
```

## 🚨 Troubleshooting

### Common Issues

1. **Static Files Not Loading**
   ```bash
   # Collect static files
   railway run python manage.py collectstatic --noinput
   ```

2. **Database Connection Error**
   - Check `DATABASE_URL` environment variable
   - Ensure PostgreSQL service is running
   - Verify database credentials

3. **Migration Issues**
   ```bash
   # Reset migrations (development only)
   railway run python manage.py migrate --fake-initial
   
   # Or run specific migration
   railway run python manage.py migrate carparks 0001 --fake
   ```

4. **Import Data Issues**
   ```bash
   # Check CSV file exists
   railway run ls -la dataset/
   
   # Run data loading script manually
   railway run python scripts/load_and_store.py
   ```

### Performance Optimization

1. **Database Optimization**
   ```python
   # Add indexes in models.py
   class Meta:
       indexes = [
           models.Index(fields=['address']),
           models.Index(fields=['car_park_type']),
       ]
   ```

2. **Caching**
   ```python
   # Add to settings.py
   CACHES = {
       'default': {
           'BACKEND': 'django.core.cache.backends.redis.RedisCache',
           'LOCATION': 'redis://127.0.0.1:6379/1',
       }
   }
   ```

3. **Gunicorn Configuration**
   ```bash
   # Optimize worker count
   gunicorn --workers $((2 * $(nproc) + 1)) AdvancedWebDevelopment.wsgi:application
   ```

## 📊 Monitoring & Analytics

### Application Metrics

1. **Add Health Check Endpoint**
   ```python
   # In views.py
   from django.http import JsonResponse
   
   def health_check(request):
       return JsonResponse({
           'status': 'healthy',
           'carparks_count': CarPark.objects.count(),
           'timestamp': timezone.now().isoformat()
       })
   ```

2. **Monitor Performance**
   - Use Railway metrics
   - Set up error tracking (Sentry)
   - Monitor database performance

### Backup Strategy

1. **Database Backup**
   ```bash
   # Railway database backup
   railway pg:dump > backup.sql
   
   # Restore from backup
   railway pg:restore < backup.sql
   ```

2. **Code Backup**
   - Regular Git commits
   - Multiple repository mirrors
   - Tagged releases

## 🎯 Next Steps

After successful deployment:

1. **Set up monitoring and alerting**
2. **Configure custom domain**
3. **Set up SSL certificate**
4. **Implement caching strategy**
5. **Add rate limiting**
6. **Set up backup procedures**
7. **Monitor performance metrics**

## 📞 Support

If you encounter issues during deployment:

1. Check the [troubleshooting section](#🚨-troubleshooting)
2. Review application logs
3. Open an issue on GitHub
4. Contact the development team

---

**Happy Deploying! 🚀**
