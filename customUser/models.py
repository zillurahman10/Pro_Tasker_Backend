from django.db import models
from django.contrib.auth.models import User

# Create your models here.
role = (
    ('client', 'Client'),
    ('freelancer', 'Freelancer')
)

class CustomUser(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    role = models.CharField(max_length=50, choices=role)