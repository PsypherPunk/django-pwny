# -*- coding: utf-8
from __future__ import unicode_literals, absolute_import
import random

import django

DEBUG = True
USE_TZ = True

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = "".join(
    [
        random.SystemRandom().choice(
            "abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*(-_=+)"
        )
        for i in range(50)
    ]
)

DATABASES = {"default": {"ENGINE": "django.db.backends.sqlite3", "NAME": ":memory:"}}

ROOT_URLCONF = "tests.urls"

INSTALLED_APPS = [
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sites",
    "pwny",
]

SITE_ID = 1

if django.VERSION >= (1, 10):
    MIDDLEWARE = ()
else:
    MIDDLEWARE_CLASSES = ()
