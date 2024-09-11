from rest_framework import serializers
from . import models

class FreelancerSerializer(serializers.ModelSerializer):
    category = serializers.SlugRelatedField(
        many=True, slug_field='slug', queryset=models.Category.objects.all()
    )
    skills = serializers.SlugRelatedField(
        many=True, slug_field='slug', queryset=models.Skills.objects.all()
    )
    # portfolio = serializers.StringRelatedField(many=True)
    
    class Meta:
        model = models.Freelancer
        fields = '__all__'

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Category
        fields = '__all__'

class SkillsSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Skills
        fields = '__all__'

class PortfolioSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Portfolio
        fields = '__all__'
