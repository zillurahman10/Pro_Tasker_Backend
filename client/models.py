from django.db import models
from django.contrib.auth.models import User
from django.contrib.auth.models import AbstractUser

# Create your models here.
countries = [
    ('USA', 'USA'),
    ('UK', 'UK'),
    ('Canada', 'Canada'),
    ('Australia', 'Australia'),
    ('India', 'India'),
    ('Bangladesh', 'Bangladesh'),
    ('China', 'China'),
    ('Germany', 'Germany'),
    ('France', 'France'),
    ('Japan', 'Japan'),
    ('South Korea', 'South Korea'),
    ('Brazil', 'Brazil'),
    ('Mexico', 'Mexico'),
    ('Russia', 'Russia'),
    ('Italy', 'Italy'),
    ('Spain', 'Spain'),
    ('Netherlands', 'Netherlands'),
    ('Sweden', 'Sweden'),
    ('Norway', 'Norway'),
    ('Denmark', 'Denmark'),
    ('South Africa', 'South Africa'),
    ('New Zealand', 'New Zealand'),
    ('Ireland', 'Ireland'),
    ('Singapore', 'Singapore'),
    ('Malaysia', 'Malaysia'),
    ('Indonesia', 'Indonesia'),
    ('Philippines', 'Philippines'),
    ('Pakistan', 'Pakistan'),
    ('Nigeria', 'Nigeria'),
    ('Kenya', 'Kenya'),
    ('Egypt', 'Egypt'),
    ('Saudi Arabia', 'Saudi Arabia'),
    ('Turkey', 'Turkey'),
    ('United Arab Emirates', 'United Arab Emirates'),
    ('Argentina', 'Argentina'),
    ('Chile', 'Chile'),
    ('Colombia', 'Colombia'),
    ('Venezuela', 'Venezuela'),
    ('Israel', 'Israel'),
    ('Poland', 'Poland'),
    ('Greece', 'Greece'),
    ('Portugal', 'Portugal'),
    ('Finland', 'Finland'),
    ('Switzerland', 'Switzerland'),
    ('Austria', 'Austria'),
    ('Belgium', 'Belgium'),
    ('Czech Republic', 'Czech Republic'),
    ('Hungary', 'Hungary'),
    ('Romania', 'Romania'),
    ('Ukraine', 'Ukraine'),
    ('Vietnam', 'Vietnam'),
    ('Thailand', 'Thailand'),
    ('Sri Lanka', 'Sri Lanka'),
    ('Nepal', 'Nepal'),
]

class Client(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.CharField(max_length=500, default="")
    country = models.CharField(max_length=50, choices=countries)

    def __str__(self):
        return self.user.username
       

    