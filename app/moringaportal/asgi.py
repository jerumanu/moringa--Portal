import os
from notifications.consumer import NotificationConsumer
from channels.routing import ProtocolTypeRouter,URLRouter
from channels.auth import AuthMiddlewareStack
from notifications import consumers

from django.urls import re_path,path
from django.core.asgi import get_asgi_application
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'moringaportal.settings')
import notifications.routing
application = ProtocolTypeRouter({
    "http": get_asgi_application(),
    "websocket":AuthMiddlewareStack(
URLRouter(
[path('notification/notifications/',NotificationConsumer.as_asgi())]
))

})