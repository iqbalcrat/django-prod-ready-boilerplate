from .base_settings import *


DEBUG = True

ALLOWED_HOSTS = env("ALLOWED_HOSTS")

SECRET_KEY = env("SECRET_KEY")


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases


DATABASES = {
    'default': {
        'ENGINE': env('DB_ENGINE'),
        'NAME': os.getenv('DB_NAME'),
        'USER': os.getenv('DB_USER'),
        'PASSWORD': os.getenv('DB_PASSWORD'),
        'HOST': os.getenv('DB_HOST'),
        'PORT': os.getenv('DB_PORT'),
    }
}



# Your production stuff: Below this line define 3rd party library settings
AWS_ACCESS_KEY_ID = env('DJANGO_AWS_ACCESS_KEY_ID')
AWS_SECRET_ACCESS_KEY = env('DJANGO_AWS_SECRET_ACCESS_KEY')
AWS_S3_HOST = env('DJANGO_AWS_S3_HOST')
AWS_STORAGE_BUCKET_NAME = env('DJANGO_AWS_STORAGE_BUCKET_NAME')
AWS_QUERYSTRING_AUTH = False


#Media & Static settings for PROD(Amazon S3 bucket)

MEDIA_LOCATION = 'media'
MEDIA_URL = env('DJANGO_MEDIA_URL',
                default='https://%s/%s/%s/' % (AWS_S3_HOST, AWS_STORAGE_BUCKET_NAME, MEDIA_LOCATION))
DEFAULT_FILE_STORAGE = 'config.settings.storages.MediaStorage'

STATIC_LOCATION = 'static'
STATIC_URL = env('DJANGO_STATIC_URL',
                 default='https://%s/%s/%s/' % (AWS_S3_HOST, AWS_STORAGE_BUCKET_NAME, STATIC_LOCATION))
STATICFILES_STORAGE = 'config.settings.storages.StaticStorage'