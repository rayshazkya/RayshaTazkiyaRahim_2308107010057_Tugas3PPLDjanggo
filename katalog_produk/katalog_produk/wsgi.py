"""
WSGI config for katalog_produk project.
"""

import os
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'katalog_produk.settings')
application = get_wsgi_application()
