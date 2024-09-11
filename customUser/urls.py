from rest_framework.routers import DefaultRouter
from django.urls import path, include
from . import views

router = DefaultRouter()

router.register('custom_users', views.CustomUserViewSet)
urlpatterns = [
    path('', include(router.urls)),
]