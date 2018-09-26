"""
WSGI config for scse_cz3003_2018_s1_cms project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.1/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'scse_cz3003_2018_s1_cms.settings')

application = get_wsgi_application()
