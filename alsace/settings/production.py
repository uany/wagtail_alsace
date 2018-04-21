import os
from .base import *

DEBUG = False
SECRET_KEY = os.getenv('SECRET_KEY')
ALLOWED_HOSTS = ['127.0.0.1', 'www.alsace.nyc', 'wagtailalsace.herokuapp.com', 'alsace.nyc']

SECURE_CONTENT_TYPE_NOSNIFF = True
SESSION_COOKIE_SECURE = True
CSRF_COOKIE_SECURE = True
X_FRAME_OPTIONS = 'DENY'
