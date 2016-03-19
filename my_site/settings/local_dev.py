import random
import string

from my_site.settings.base_settings import *


SECRET_KEY = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(20))

STATIC_ROOT = os.path.join(PROJECT_DIR, "../public/static")
MEDIA_ROOT = os.path.join(PROJECT_DIR, "../public/media")
