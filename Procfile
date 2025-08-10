web: python manage.py migrate && python manage.py collectstatic --noinput && gunicorn --bind 0.0.0.0:$PORT AdvancedWebDevelopment.wsgi:application
release: python scripts/load_and_store.py
