from rest_framework.routers import DefaultRouter
from django.urls import path, include
from . import views

router = DefaultRouter()

router.register('freelancers', views.FreelancerViewSet)
router.register('categories', views.CategoryViewSet)
router.register('skills', views.SkillViewSet)
router.register('portfolios', views.PortfolioViewSet)
urlpatterns = [
    path('', include(router.urls)),
]
