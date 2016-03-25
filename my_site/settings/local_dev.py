from my_site.settings.base_settings import *


ALLOWED_HOSTS = ['localhost:8001']

DEBUG = True

STATIC_ROOT = os.path.join(PROJECT_DIR, "../public/static")
MEDIA_ROOT = os.path.join(PROJECT_DIR, "../public/media")
