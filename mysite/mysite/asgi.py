"""
ASGI config for mysite project.

It exposes the ASGI callable as a module-level variable named ``application``.
ASGI는 곧 WSGI에 대한 호환성을 가지면서 비동기적인 요청을 처리할 수 있는 인터페이스입니다.

For more information on this file, see
https://docs.djangoproject.com/en/5.0/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "mysite.settings")

application = get_asgi_application()
