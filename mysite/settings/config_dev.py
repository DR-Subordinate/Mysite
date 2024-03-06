from .base import *

SECRET_KEY = "django-insecure-8#7=val(t$hzrxw*9z31#g_esk9z518&$7m9u&mozt8&y0225d"

DEBUG = True

ALLOWED_HOSTS = ["localhost"]

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": BASE_DIR / "db.sqlite3",
    }
}
