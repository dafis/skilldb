from .base import *

# Deploy a production instance: 
# https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

DEBUG = False

try:
    from .local import *
except ImportError:
    pass
