from pathlib import Path
import os
try:
    import dj_database_url  # type: ignore
except ModuleNotFoundError:
    dj_database_url = None  # Will only be required when DATABASE_URL is used
from django.core.exceptions import ImproperlyConfigured

BASE_DIR = Path(__file__).resolve().parent.parent

# ----- Environment helpers -----------------------------------------------------
def _to_bool(v, default=False):
    if v is None:
        return default
    return str(v).strip().lower() in {"1", "true", "yes", "y", "on"}

# Detect environment: "production" or "development"
DJANGO_ENV = (
    os.getenv("DJANGO_ENV")
    or os.getenv("RAILWAY_ENVIRONMENT")
    or ("production" if os.getenv("GITHUB_ACTIONS") else "development")
).strip().lower()
IS_PROD = DJANGO_ENV == "production"

# ----- Core --------------------------------------------------------------------
SECRET_KEY = os.getenv("DJANGO_SECRET_KEY") or os.getenv("SECRET_KEY", "change-me-in-prod")
DEBUG = _to_bool(os.getenv("DJANGO_DEBUG") or os.getenv("DEBUG"), default=not IS_PROD)
ALLOWED_HOSTS = [h.strip() for h in os.getenv("ALLOWED_HOSTS", "*").split(",") if h.strip()]

# ----- Apps --------------------------------------------------------------------
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "carparks",
    "rest_framework",
    "corsheaders",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "corsheaders.middleware.CorsMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "AdvancedWebDevelopment.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [BASE_DIR / "templates"],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "AdvancedWebDevelopment.wsgi.application"

# ----- Database: Prod requires Postgres; Dev can use SQLite --------------------
db_ssl_required = _to_bool(os.getenv("DB_SSL_REQUIRED"), default=False)
database_url = os.getenv("DATABASE_URL")

if IS_PROD:
    # Production MUST have DATABASE_URL (Postgres)
    if not database_url:
        raise ImproperlyConfigured(
            "DATABASE_URL is required in production. "
            "Set it in Railway (pointing to Postgres)."
        )
    if dj_database_url is None:
        raise ImproperlyConfigured(
            "dj-database-url is not installed. Run 'pip install dj-database-url' or add it to your environment."
        )
    DATABASES = {
        "default": dj_database_url.parse(database_url, conn_max_age=600, ssl_require=db_ssl_required)
    }
else:
    # Development: use DATABASE_URL if present, otherwise SQLite
    if database_url:
        if dj_database_url is None:
            raise ImproperlyConfigured(
                "dj-database-url is not installed. Run 'pip install dj-database-url' or add it to your environment."
            )
        DATABASES = {
            "default": dj_database_url.parse(database_url, conn_max_age=600, ssl_require=db_ssl_required)
        }
    else:
        DATABASES = {
            "default": {
                "ENGINE": "django.db.backends.sqlite3",
                "NAME": BASE_DIR / "db.sqlite3",
            }
        }

# ----- Password validation -----------------------------------------------------
AUTH_PASSWORD_VALIDATORS = [
    {"NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"},
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]

# ----- i18n --------------------------------------------------------------------
LANGUAGE_CODE = "en-us"
TIME_ZONE = "UTC"
USE_I18N = True
USE_TZ = True

# ----- Static / WhiteNoise -----------------------------------------------------
STATIC_URL = "/static/"
STATIC_ROOT = BASE_DIR / "staticfiles"
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

# ----- Proxy / Security --------------------------------------------------------
SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")

# CSRF trusted origins (singular or plural supported)
_raw_csrf = (
    os.getenv("CSRF_TRUSTED_ORIGINS")
    or os.getenv("CSRF_TRUSTED_ORIGIN")
    or "https://*"
)
CSRF_TRUSTED_ORIGINS = [o.strip() for o in _raw_csrf.split(",") if o.strip()]

# CORS (optional)
_raw_cors = os.getenv("CORS_ALLOWED_ORIGINS", "")
if _raw_cors:
    CORS_ALLOWED_ORIGINS = [o.strip() for o in _raw_cors.split(",") if o.strip()]
CORS_ALLOW_CREDENTIALS = True

# REST framework defaults
REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": [
        "rest_framework.authentication.SessionAuthentication",
        "rest_framework.authentication.BasicAuthentication",
    ],
    "DEFAULT_PERMISSION_CLASSES": ["rest_framework.permissions.AllowAny"],
}

# Extra hardening when NOT DEBUG (usually production)
if not DEBUG:
    SESSION_COOKIE_SECURE = True
    CSRF_COOKIE_SECURE = True
    SECURE_CONTENT_TYPE_NOSNIFF = True
    X_FRAME_OPTIONS = "DENY"
    # HSTS can be enabled once you’re sure HTTPS is always used:
    SECURE_HSTS_SECONDS = int(os.getenv("SECURE_HSTS_SECONDS", "0"))
    SECURE_HSTS_INCLUDE_SUBDOMAINS = _to_bool(os.getenv("SECURE_HSTS_INCLUDE_SUBDOMAINS"), default=False)
    SECURE_HSTS_PRELOAD = _to_bool(os.getenv("SECURE_HSTS_PRELOAD"), default=False)

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
