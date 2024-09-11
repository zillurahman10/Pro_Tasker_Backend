from django.shortcuts import render
from rest_framework import viewsets, filters
from . import models
from . import serializers

# Create your views here.
class CustomUserViewSet(viewsets.ModelViewSet):
    queryset = models.ClientReviews.objects.all()
    serializer_class = serializers.ReviewSerializer