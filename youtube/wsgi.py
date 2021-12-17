"""
WSGI config for youtube project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/howto/deployment/wsgi/
"""

import os
from threading import Thread
from django.core.wsgi import get_wsgi_application
from api.utils import get_youtube_api_detail

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "youtube.settings")

application = get_wsgi_application()

# Thread for get_youtube_api_details
Thread(target=get_youtube_api_detail, args=()).start()
