from my_site.base_settings import *


with open('/etc/my_site/secret_key.txt') as f:
    SECRET_KEY = f.read().strip()

STATIC_ROOT = '/var/www/my_site/static'
MEDIA_ROOT = '/var/www/my_site/media'

