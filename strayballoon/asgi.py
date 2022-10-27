from channels.routing import ProtocolTypeRouter, URLRouter
from channels.security.websocket import AllowedHostsOriginValidator

import strayballoon.urls
from strayballoon.middleware import TokenAuthMiddleware

"""
ASGI config for strayballoon project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/howto/deployment/asgi/
"""

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'strayballoon.settings')

django_asgi_app = get_asgi_application()

import strayballoon.urls

application = ProtocolTypeRouter({
    "http": django_asgi_app,
    "websocket": AllowedHostsOriginValidator(
        TokenAuthMiddleware(URLRouter(strayballoon.urls.websocket_urlpatterns))
    ),
})
