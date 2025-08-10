@echo off
echo ===============================================
echo  Carpark API - Windows Development Setup
echo ===============================================
echo.

echo [1/5] Installing all dependencies from requirements.txt...
pip install -r requirements.txt

echo.
echo [2/5] Installing optional development tools...
pip install black isort flake8 --quiet
echo Note: Development tools are optional and errors can be ignored.

echo.
echo [3/5] Running Django system check...
python manage.py check

echo.
echo [4/5] Running database migrations...
python manage.py migrate

echo.
echo [5/5] Loading sample data...
python scripts/load_and_store.py

echo.
echo ===============================================
echo  Installation Complete!
echo ===============================================
echo.
echo To start the development server, run:
echo   python manage.py runserver
echo.
echo Then visit: http://localhost:8000/api/v1/carparks/
echo.
pause
