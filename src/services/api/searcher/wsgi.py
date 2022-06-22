from django.core.handlers.wsgi import WSGIHandler
from django.core.wsgi import get_wsgi_application

application: WSGIHandler = get_wsgi_application()
