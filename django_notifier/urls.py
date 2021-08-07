from django.contrib import admin
from django.urls import path
from rest_framework import routers
from django.urls import path, include
from notifier.views import HandleGetWayViewSet

router = routers.DefaultRouter()
router.register(r'get_way', HandleGetWayViewSet, basename='get_way')

urlpatterns: list = [
    path('api/', include(router.urls)),
]

