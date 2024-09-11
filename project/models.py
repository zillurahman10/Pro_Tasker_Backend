from django.db import models
from client.models import Client
from freelancer.models import Freelancer
from freelancer.models import Category

ratings = [
    ('⭐','⭐'),
    ('⭐⭐','⭐⭐'),
    ('⭐⭐⭐','⭐⭐⭐'),
    ('⭐⭐⭐⭐','⭐⭐⭐⭐'),
    ('⭐⭐⭐⭐⭐','⭐⭐⭐⭐⭐'),
]
# Create your models here.
class Project(models.Model):
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    description = models.TextField(max_length=550)
    budget = models.IntegerField()
    deadline = models.DateTimeField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE, blank=True, default=None, null=True)
    project_requirements = models.TextField(max_length=1000)
    attachments = models.CharField(max_length=500, default="")
    is_completed = models.BooleanField(default=False)

    # def __str__(self):
    #     return self.title
    
class ClientReviews(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    freelancer = models.ForeignKey(Freelancer, on_delete=models.CASCADE)
    review_text = models.TextField(max_length=500)
    rating = models.CharField(max_length=10, choices=ratings)
