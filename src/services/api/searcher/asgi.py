from django.core.asgi import get_asgi_application
from django.core.handlers.asgi import ASGIHandler

application: ASGIHandler = get_asgi_application()
