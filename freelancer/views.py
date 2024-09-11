from django.shortcuts import render
from rest_framework import viewsets, filters
from . import models
from . import serializers

# Create your views here.
class FreelancerViewSet(viewsets.ModelViewSet):
    queryset = models.Freelancer.objects.all()
    serializer_class = serializers.FreelancerSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['user__first_name', 'user__last_name', 'category__category_name', 'skills__skill_name']

class PortfolioViewSet(viewsets.ModelViewSet):
    queryset = models.Portfolio.objects.all()
    serializer_class = serializers.PortfolioSerializer
    

class CategoryViewSet(viewsets.ModelViewSet):
    queryset = models.Category.objects.all()
    serializer_class = serializers.CategorySerializer

class SkillViewSet(viewsets.ModelViewSet):
    queryset = models.Skills.objects.all()
    serializer_class = serializers.SkillsSerializer