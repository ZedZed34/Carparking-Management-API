# 🚗 Carpark Management API

A modern Django REST API for managing carpark information with comprehensive features, Docker containerization, and automated CI/CD deployment to Railway.

[![CI/CD Pipeline](https://github.com/ZedZed34/Carparking-Management-API/actions/workflows/deploy.yml/badge.svg)](https://github.com/ZedZed34/Carparking-Management-API/actions/workflows/deploy.yml)
[![Test Suite](https://github.com/ZedZed34/Carparking-Management-API/actions/workflows/test.yml/badge.svg)](https://github.com/ZedZed34/Carparking-Management-API/actions/workflows/test.yml)

## 🌟 **Features**

### Core Functionality
- **📋 View All Carparks**: List all carparks with pagination support
- **🔍 Filter by Car Park Type**: Filter carparks by specific types
- **🆓 Filter Free Parking**: Find carparks offering free parking
- **📊 Group by Parking System**: Display grouped statistics by parking system
- **📏 Average Gantry Height**: Calculate and display average gantry heights
- **➕ Add New Car Park**: Create new carpark entries via REST API
- **🔎 Search by Address**: Advanced address-based search functionality
- **📐 Height Range Filter**: Filter carparks by gantry height range

### Technical Features
- ✅ **RESTful API** with comprehensive endpoints
- ✅ **Docker containerization** for easy deployment
- ✅ **Automated CI/CD** with GitHub Actions
- ✅ **Railway deployment** ready
- ✅ **PostgreSQL support** for production
- ✅ **Nginx reverse proxy** configuration
- ✅ **Security best practices** implemented
- ✅ **API documentation** with Django REST Framework
- ✅ **Input validation** and error handling
- ✅ **Health checks** and monitoring

---

## 🚀 **Quick Start**

### Option 1: Docker (Recommended)

```bash
# Clone the repository
git clone https://github.com/ZedZed34/Carparking-Management-API.git
cd Carparking-Management-API

# Start with Docker Compose
docker-compose up --build

# Access the application
open http://localhost
```

### Option 2: Local Development

#### For Linux/Mac:
```bash
# Clone and navigate
git clone https://github.com/ZedZed34/Carparking-Management-API.git
cd Carparking-Management-API

# Create virtual environment
python -m venv venv
source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Set up database
python manage.py migrate

# Load sample data
python scripts/load_and_store.py

# Run development server
python manage.py runserver
```

#### For Windows:
```bash
# Clone and navigate
git clone https://github.com/ZedZed34/Carparking-Management-API.git
cd "Carparking-Management-API"

# Create virtual environment
python -m venv HLA
HLA\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Or use the automated installer
install_dev.bat

# Set up database
python manage.py migrate

# Load sample data
python scripts/load_and_store.py

# Run development server
python manage.py runserver
```

> **Note**: If you encounter PostgreSQL installation issues on Windows, the app will automatically use SQLite for development. See [WINDOWS_SETUP.md](WINDOWS_SETUP.md) for troubleshooting.

---

## 🔧 **Requirements**

### System Requirements
- **Python**: 3.10+ (3.11 recommended)
- **Database**: SQLite (development) / PostgreSQL (production)
- **Docker**: Optional but recommended

### Dependencies
- Django 5.2.5
- Django REST Framework 3.15.2
- Gunicorn (production server)
- WhiteNoise (static files)
- psycopg2-binary (PostgreSQL)
- pandas & numpy (data processing)

---

## 📖 **API Documentation**

### Base URL
- **Development**: `http://localhost:8000/api/v1/`
- **Production**: `https://your-railway-app.railway.app/api/v1/`

### Available Endpoints

| Endpoint | Method | Description |
|----------|---------|-------------|
| `/carparks/` | GET | List all carparks (paginated) |
| `/carparks/` | POST | Create a new carpark |
| `/carparks/{id}/` | GET/PUT/PATCH | Retrieve/update specific carpark |
| `/carparks/filter/?type={type}` | GET | Filter by carpark type |
| `/carparks/free/` | GET | Get carparks with free parking |
| `/carparks/search/?address={query}` | GET | Search by address |
| `/carparks/group/` | GET | Group by parking system |
| `/carparks/average/` | GET | Get average gantry height |
| `/carparks/height-range/` | GET | Filter by height range |
| `/carparks/types/` | GET | Get all carpark types |

### Example Requests

```bash
# Get all carparks
curl -X GET "http://localhost:8000/api/v1/carparks/"

# Filter by type
curl -X GET "http://localhost:8000/api/v1/carparks/filter/?type=SURFACE%20CAR%20PARK"

# Search by address
curl -X GET "http://localhost:8000/api/v1/carparks/search/?address=clementi"

# Create new carpark
curl -X POST "http://localhost:8000/api/v1/carparks/" \
  -H "Content-Type: application/json" \
  -d '{
    "address": "123 Test Street",
    "car_park_type": "SURFACE CAR PARK",
    "gantry_height": 2.5,
    "night_parking": true
  }'
```

---

## 🐳 **Docker Deployment**

### Local Development with Docker

```bash
# Build and run
docker-compose up --build

# Run in background
docker-compose up -d

# View logs
docker-compose logs -f

# Stop services
docker-compose down
```

### Production Docker Build

```bash
# Build production image
docker build -t carpark-api .

# Run production container
docker run -p 8000:8000 \
  -e SECRET_KEY="your-secret-key" \
  -e DEBUG=False \
  -e DATABASE_URL="postgresql://..." \
  carpark-api
```

---

## 🚂 **Railway Deployment**

### Automatic Deployment (Recommended)

1. **Fork this repository**
2. **Connect to Railway**:
   - Go to [Railway](https://railway.app)
   - Create new project from GitHub repo
   - Select your forked repository

3. **Set Environment Variables** in Railway dashboard:
   ```
   SECRET_KEY=your-super-secret-key-here
   DEBUG=False
   ALLOWED_HOSTS=*.railway.app
   ```

4. **Add PostgreSQL service**:
   - In Railway dashboard, click "Add Service"
   - Select "PostgreSQL"
   - Railway will automatically set `DATABASE_URL`

5. **Deploy**: Railway will automatically deploy on every push to main branch

### Manual Deployment

```bash
# Install Railway CLI
curl -fsSL https://railway.app/install.sh | sh

# Login and deploy
railway login
railway init
railway up
```

---

## ⚙️ **CI/CD Pipeline**

### GitHub Actions Workflows

This project includes comprehensive CI/CD pipelines:

#### 1. **Test Pipeline** (`.github/workflows/test.yml`)
- ✅ **Linting**: flake8, black, isort
- ✅ **Multi-version testing**: Python 3.10, 3.11, 3.12
- ✅ **Security scanning**: safety, bandit
- ✅ **Coverage reporting**: codecov integration
- ✅ **Database testing**: PostgreSQL integration

#### 2. **Deployment Pipeline** (`.github/workflows/deploy.yml`)
- ✅ **Automated testing**: Full test suite
- ✅ **Docker build**: Multi-platform images
- ✅ **Railway deployment**: Automatic deployment
- ✅ **Post-deployment**: Database migrations and data loading
- ✅ **Notifications**: Status reporting

### Required Secrets

Set these in your GitHub repository settings:

```
DOCKER_USERNAME=your-dockerhub-username
DOCKER_PASSWORD=your-dockerhub-password
RAILWAY_TOKEN=your-railway-api-token
```

---

## 🛠️ **Development**

### Project Structure
```
Carparking-Management-API/
├── AdvancedWebDevelopment/     # Django project settings
├── carparks/                   # Main application
│   ├── models.py              # CarPark model with validation
│   ├── serializers.py         # API serializers
│   ├── views.py               # API views and endpoints
│   ├── urls.py                # URL routing
│   └── templates/             # HTML templates
├── scripts/                    # Data management scripts
├── dataset/                    # CSV data files
├── .github/workflows/          # CI/CD pipelines
├── docker-compose.yml          # Docker development setup
├── Dockerfile                  # Production container
├── railway.json               # Railway configuration
└── requirements.txt           # Python dependencies
```

### Running Tests

```bash
# Run all tests
python manage.py test

# Run with coverage
pip install coverage
coverage run --source='.' manage.py test
coverage report

# Run specific test
python manage.py test carparks.tests.TestCarParkAPI
```

### Code Quality

```bash
# Format code
pip install black isort
black --line-length=127 .
isort --profile black .

# Lint code
pip install flake8
flake8 . --max-line-length=127

# Security check
pip install bandit safety
bandit -r .
safety check
```

---

## 🔒 **Security Features**

- ✅ **Environment-based configuration**
- ✅ **Secret key management**
- ✅ **HTTPS enforcement** in production
- ✅ **Security headers** (XSS, CSRF protection)
- ✅ **Input validation** and sanitization
- ✅ **Rate limiting** ready
- ✅ **SQL injection prevention**
- ✅ **CORS configuration**

---

## 📊 **Monitoring & Health Checks**

### Health Check Endpoint
```bash
# Check application health
curl http://localhost:8000/api/v1/carparks/
```

### Docker Health Check
The Docker container includes automatic health checks:
```dockerfile
HEALTHCHECK --interval=30s --timeout=30s --start-period=5s --retries=3 \
    CMD curl -f http://localhost:8000/api/v1/carparks/ || exit 1
```

---

## 🤝 **Contributing**

1. **Fork the repository**
2. **Create feature branch**: `git checkout -b feature/amazing-feature`
3. **Commit changes**: `git commit -m 'Add amazing feature'`
4. **Push to branch**: `git push origin feature/amazing-feature`
5. **Open Pull Request**

### Development Guidelines
- Follow PEP 8 style guide
- Write comprehensive tests
- Update documentation
- Ensure CI/CD passes

---

## 📄 **License**

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---

## 📞 **Support & Contact**

- **GitHub Issues**: [Report bugs or request features](https://github.com/ZedZed34/Carparking-Management-API/issues)
- **Documentation**: [View full API docs](https://your-railway-app.railway.app/api/v1/)
- **Email**: your-email@example.com

---

## 🙏 **Acknowledgments**

- Django REST Framework team
- Railway platform
- GitHub Actions
- Docker community
- HDB Singapore for the dataset

---

