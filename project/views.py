from django.shortcuts import render
from rest_framework import viewsets, filters
from . import models
from . import serializers

# Create your views here.
class ProjectViewSet(viewsets.ModelViewSet):
    queryset = models.Project.objects.all()
    serializer_class = serializers.ProjectSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['category__category_name', 'title']

class ReviewViewSet(viewsets.ModelViewSet):
    queryset = models.ClientReviews.objects.all()
    serializer_class = serializers.ReviewSerializer