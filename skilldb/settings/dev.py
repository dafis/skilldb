from .base import *

DEBUG = True
SECRET_KEY = 'django-insecure---gs(3=^01rcs^yr#k4@pgvt!hg(g46r#_cc^rg6jcuuy+$eb$'
ALLOWED_HOSTS = ['*'] 
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

try:
    from .local import *  # noqa
except ImportError:
    pass
