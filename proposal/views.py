from django.shortcuts import render
from rest_framework import viewsets, filters
from . import models
from . import serializers

# Create your views here.
class ProposalViewSet(viewsets.ModelViewSet):
    queryset = models.Proposal.objects.all()
    serializer_class = serializers.ProposalSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['freelancer']