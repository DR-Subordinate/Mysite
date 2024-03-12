import os

from .base import *

SECRET_KEY = os.environ["SECRET_KEY"]

DEBUG = True

ALLOWED_HOSTS = ["test.across-shop.com"]

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.mysql",
        "HOST": os.environ["DATABASE_HOST"],
        "PORT": os.environ["DATABASE_PORT"],
        "NAME": os.environ["DATABASE_NAME_TEST"],
        "USER": os.environ["DATABASE_USERNAME_TEST"],
        "PASSWORD": os.environ["DATABASE_PASSWORD_TEST"],
        "TEST": {
            "NAME": os.environ["DATABASE_NAME_UNITTEST"],
        },
        "OPTIONS": {
            "init_command": "SET sql_mode='STRICT_TRANS_TABLES'",
        },
    },
}

# DATABASES = {
#     "default": {
#         "ENGINE": "django.db.backends.sqlite3",
#         "NAME": BASE_DIR / "db.sqlite3",
#     }
# }

STATIC_ROOT = BASE_DIR / "static/"
