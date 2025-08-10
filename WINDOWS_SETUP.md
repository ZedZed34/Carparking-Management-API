# 🪟 Windows Development Setup Guide

This guide helps you set up the Carpark Management API on Windows, addressing common issues with dependencies.

## 🚨 Current Issues & Solutions

### Issue 1: psycopg2-binary Build Failure
**Problem**: psycopg2-binary fails to compile on Windows due to missing PostgreSQL development libraries.

**Solution**: For local development, we'll use SQLite (no PostgreSQL needed).

### Issue 2: Missing Production Dependencies
**Problem**: whitenoise, gunicorn, and other production dependencies aren't installed.

**Solution**: Install only what's needed for development.

## 🔧 Quick Fix Steps

### Step 1: Install Dependencies
```bash
# Install all dependencies from the single requirements file
pip install -r requirements.txt

# If you encounter PostgreSQL issues, the app will automatically
# fall back to SQLite for development (no additional action needed)
```

### Step 2: Test the Installation
```bash
# Run the test script
python test_installation.py

# Or manually test Django
python manage.py check
```

### Step 3: Run the Development Server
```bash
# Start the server
python manage.py runserver

# Visit the API
# http://localhost:8000/api/v1/carparks/
```

## 📦 Install Script for Windows

Create a file called `install_dev.bat` with this content:

```batch
@echo off
echo Installing Carpark API for Windows Development...

echo.
echo Installing core Django dependencies...
pip install Django==5.2.5
pip install djangorestframework==3.15.2
pip install asgiref==3.9.1
pip install sqlparse==0.5.3

echo.
echo Installing data processing libraries...
pip install numpy==2.3.2
pip install pandas==2.3.1
pip install python-dateutil==2.9.0.post0
pip install pytz==2025.2

echo.
echo Installing HTTP and utility libraries...
pip install requests==2.32.4
pip install certifi==2025.8.3
pip install python-dotenv==1.0.1

echo.
echo Testing installation...
python test_installation.py

echo.
echo Starting development server...
python manage.py runserver
```

## 🔍 Troubleshooting

### If Django won't start:
1. **Check your virtual environment is activated**:
   ```bash
   # Windows
   HLA\Scripts\activate
   
   # Should show (HLA) in your prompt
   ```

2. **Check Django installation**:
   ```bash
   python -c "import django; print(django.get_version())"
   ```

3. **Run system check**:
   ```bash
   python manage.py check
   ```

### If you get import errors:
1. **Missing modules**: Install them individually
   ```bash
   pip install <module-name>
   ```

2. **Path issues**: Make sure you're in the project directory
   ```bash
   cd "D:\Carpark Django API"
   ```

### If you need PostgreSQL later:
1. **Install PostgreSQL**: Download from https://www.postgresql.org/download/windows/
2. **Install psycopg2**: 
   ```bash
   pip install psycopg2-binary
   ```
   If it fails, try:
   ```bash
   pip install psycopg2 --no-cache-dir
   ```

## 🚀 Production vs Development

### Development (Windows)
- ✅ SQLite database (no setup required)
- ✅ Django development server
- ✅ No Docker required
- ✅ Minimal dependencies

### Production (Docker/Railway)
- ✅ PostgreSQL database
- ✅ Gunicorn WSGI server
- ✅ WhiteNoise for static files
- ✅ Full security features

## 📝 Environment Variables

For development, create a `.env` file in the project root:

```env
# Development settings
DEBUG=True
SECRET_KEY=dev-secret-key-for-local-development-only
ALLOWED_HOSTS=localhost,127.0.0.1

# Database (leave empty to use SQLite)
DATABASE_URL=
```

## 🧪 Testing the API

Once the server is running, test these endpoints:

```bash
# List all carparks
curl http://localhost:8000/api/v1/carparks/

# Get carpark types
curl http://localhost:8000/api/v1/carparks/types/

# Search by address
curl "http://localhost:8000/api/v1/carparks/search/?address=clementi"

# Filter by type
curl "http://localhost:8000/api/v1/carparks/filter/?type=SURFACE%20CAR%20PARK"
```

Or visit in your browser:
- http://localhost:8000/api/v1/carparks/
- http://localhost:8000/home/

## ⚡ Quick Commands

```bash
# Full setup (run these in order)
git clone <your-repo>
cd "Carpark Django API"
python -m venv HLA
HLA\Scripts\activate
pip install -r requirements.txt
python manage.py migrate
python scripts/load_and_store.py
python manage.py runserver
```

## 🆘 Need Help?

1. **Check the error logs** in the terminal
2. **Run the test script**: `python test_installation.py`
3. **Check Django documentation**: https://docs.djangoproject.com/
4. **Create an issue** on GitHub with your error message

## ✅ Success Checklist

- [ ] Virtual environment activated
- [ ] Core dependencies installed
- [ ] Django check passes (`python manage.py check`)
- [ ] Database migrated (`python manage.py migrate`)
- [ ] Data loaded (`python scripts/load_and_store.py`)
- [ ] Server starts (`python manage.py runserver`)
- [ ] API responds (`curl http://localhost:8000/api/v1/carparks/`)

Once all items are checked, you're ready to develop! 🎉
