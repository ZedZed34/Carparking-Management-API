from pathlib import Path
import os
import dj_database_url

BASE_DIR = Path(__file__).resolve().parent.parent

# ── Core ────────────────────────────────────────────────────────────────────────
# Accept both DJANGO_* and legacy names for compatibility with existing env files
SECRET_KEY = os.getenv("DJANGO_SECRET_KEY") or os.getenv("SECRET_KEY", "change-me-in-prod")

def _to_bool(v: str, default: bool = False) -> bool:
    if v is None:
        return default
    return str(v).strip().lower() in {"1", "true", "yes", "y", "on"}

DEBUG = _to_bool(os.getenv("DJANGO_DEBUG") or os.getenv("DEBUG"), default=False)

# Comma-separated, trims whitespace
ALLOWED_HOSTS = [h.strip() for h in os.getenv("ALLOWED_HOSTS", "*").split(",") if h.strip()]

# ── Apps ────────────────────────────────────────────────────────────────────────
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    # your apps:
    "carparks",
    "rest_framework",
    # optional but installed in requirements
    "corsheaders",
]

# ── Middleware (WhiteNoise after Security, CORS near the top) ───────────────────
MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",  # static files in prod
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

# ── Database: use DATABASE_URL when present; fallback SQLite for local ──────────
# Set DB_SSL_REQUIRED=false when using Railway's internal hostname; true for public endpoint.
_db_ssl_required = _to_bool(os.getenv("DB_SSL_REQUIRED"), default=True)
DATABASES = {
    "default": dj_database_url.config(
        default=f"sqlite:///{BASE_DIR / 'db.sqlite3'}",
        conn_max_age=600,
        ssl_require=_db_ssl_required,
    )
}

# ── Password validation ─────────────────────────────────────────────────────────
AUTH_PASSWORD_VALIDATORS = [
    {"NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator"},
    {"NAME": "django.contrib.auth.password_validation.MinimumLengthValidator"},
    {"NAME": "django.contrib.auth.password_validation.CommonPasswordValidator"},
    {"NAME": "django.contrib.auth.password_validation.NumericPasswordValidator"},
]

# ── Internationalization ───────────────────────────────────────────────────────
LANGUAGE_CODE = "en-us"
TIME_ZONE = "UTC"
USE_I18N = True
USE_TZ = True

# ── Static files: WhiteNoise + collected into /staticfiles ─────────────────────
STATIC_URL = "/static/"
STATIC_ROOT = BASE_DIR / "staticfiles"
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

# ── Security for reverse proxy (Railway) ───────────────────────────────────────
SECURE_PROXY_SSL_HEADER = ("HTTP_X_FORWARDED_PROTO", "https")

# CSRF trusted origins — accept singular or plural env var names
_raw_csrf = (
    os.getenv("CSRF_TRUSTED_ORIGINS")  # plural (Railway UI default)
    or os.getenv("CSRF_TRUSTED_ORIGIN")  # singular (older configs)
    or "https://*"  # permissive fallback (you can tighten this)
)
CSRF_TRUSTED_ORIGINS = [o.strip() for o in _raw_csrf.split(",") if o.strip()]

# Optional: CORS (if you need browser clients hitting your API)
_raw_cors = os.getenv("CORS_ALLOWED_ORIGINS", "")
if _raw_cors:
    CORS_ALLOWED_ORIGINS = [o.strip() for o in _raw_cors.split(",") if o.strip()]
CORS_ALLOW_CREDENTIALS = True

# ── REST framework (light defaults; adjust to your needs) ───────────────────────
REST_FRAMEWORK = {
    "DEFAULT_AUTHENTICATION_CLASSES": [
        "rest_framework.authentication.SessionAuthentication",
        "rest_framework.authentication.BasicAuthentication",
    ],
    "DEFAULT_PERMISSION_CLASSES": ["rest_framework.permissions.AllowAny"],
}

# ── Production hardening when DEBUG=False ───────────────────────────────────────
if not DEBUG:
    SESSION_COOKIE_SECURE = True
    CSRF_COOKIE_SECURE = True
    SECURE_HSTS_SECONDS = int(os.getenv("SECURE_HSTS_SECONDS", "0"))  # set e.g. 31536000 once you're ready
    SECURE_HSTS_INCLUDE_SUBDOMAINS = _to_bool(os.getenv("SECURE_HSTS_INCLUDE_SUBDOMAINS"), default=False)
    SECURE_HSTS_PRELOAD = _to_bool(os.getenv("SECURE_HSTS_PRELOAD"), default=False)
    SECURE_CONTENT_TYPE_NOSNIFF = True
    SECURE_BROWSER_XSS_FILTER = True
    X_FRAME_OPTIONS = "DENY"

# ── Default PK / Auto Field ────────────────────────────────────────────────────
DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
