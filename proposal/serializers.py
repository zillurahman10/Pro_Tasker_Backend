from rest_framework import serializers
from . import models

class ProposalSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Proposal
        fields = '__all__'