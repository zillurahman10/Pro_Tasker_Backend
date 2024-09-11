from django.db import models
from freelancer.models import Freelancer
from client.models import Client
from project.models import Project

# Create your models here.
class Proposal(models.Model):
    project = models.ForeignKey(Project, on_delete=models.CASCADE)
    client = models.ForeignKey(Client, on_delete=models.CASCADE)
    freelancer = models.ForeignKey(Freelancer, on_delete=models.CASCADE)
    bid = models.IntegerField()
    cover_letter = models.TextField(max_length=500)
    status = models.CharField(max_length=100, choices=[('Pending', 'Pending'), ('Accepted', 'Accepted'), ('Completed', 'Completed')], default='Pending')
    

