from .base_settings import *


DEBUG = True

ALLOWED_HOSTS = env("ALLOWED_HOSTS")

SECRET_KEY = env("SECRET_KEY")


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

#Uses defulat sqlite3 in development
DATABASES = {
    'default': {
        'ENGINE': env('DB_ENGINE'),
        'NAME': BASE_DIR / os.getenv('DB_NAME'),
        'USER': os.getenv('DB_USER'),
        'PASSWORD': os.getenv('DB_PASSWORD'),
        'HOST': os.getenv('DB_HOST'),
        'PORT': os.getenv('DB_PORT'),
    }
}


STATIC_URL = '/static/'

STATICFILES_DIRS = [
    BASE_DIR / "static",
]