"""
ASGI config for azureDeploy project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/howto/deployment/asgi/
"""

import os
import django
from django.core.asgi import get_asgi_application
from channels.routing import ProtocolTypeRouter, URLRouter
from channels.auth import AuthMiddlewareStack
import room.routing

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'azureDeploy.settings')

application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    "websocket": AuthMiddlewareStack(
        URLRouter(
            room.routing.websocket_urlpatterns
        )
    )
})


# import os
# print("DJANGO_SETTINGS_MODULE:", os.getenv('DJANGO_SETTINGS_MODULE'))


# from django.core.asgi import get_asgi_application

# from channels.auth import AuthMiddlewareStack
# from channels.routing import ProtocolTypeRouter, URLRouter

# import room.routing

# os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'azureDeploy.settings')

# application = ProtocolTypeRouter({
#     "http" : get_asgi_application(),
#     "websocket" : AuthMiddlewareStack(
#         URLRouter(
#             room.routing.websocket_urlpatterns
#         )
#     )
# })
