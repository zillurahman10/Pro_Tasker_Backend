from rest_framework.routers import DefaultRouter
from django.urls import path, include
from . import views

router = DefaultRouter()

router.register('clients', views.ClientViewSet)
router.register('users', views.UserViewSet)
urlpatterns = [
    path('', include(router.urls)),
]
