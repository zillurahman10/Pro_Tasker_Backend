from django.db import models
from django.contrib.auth.models import User

# Create your models here.

ratings = [
    ('✩', '✩'),
    ('✩✩', '✩✩'),
    ('✩✩✩', '✩✩✩'),
    ('✩✩✩✩', '✩✩✩✩'),
    ('✩✩✩✩✩', '✩✩✩✩✩'),
]

class Skills(models.Model):
    skill_name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100)

    def __str__(self) -> str:
        return self.skill_name

class Category(models.Model):
    image = models.ImageField(upload_to='images', blank=True, null=True)
    category_name = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100)

    def __str__(self) -> str:
        return self.category_name

class Portfolio(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(max_length=500)
    image = models.CharField(max_length=500, default="")
    link = models.URLField()

    def __str__(self) -> str:
        return self.name

class Freelancer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.CharField(max_length=500, default="")
    skills = models.ManyToManyField(Skills, blank='true', default=None)
    category = models.ManyToManyField(Category, blank='true', default=None)
    descriptions = models.CharField(max_length=500, blank=True, default=None)
    rating = models.CharField(max_length=500, choices=ratings, blank=True, default=('✩', '✩') )
    location = models.CharField(max_length=100, blank=True, default=None)
    portfilio = models.ForeignKey(Portfolio, on_delete=models.CASCADE, blank=True, default=None)

    def __str__(self) -> str:
        return self.user.username
    


