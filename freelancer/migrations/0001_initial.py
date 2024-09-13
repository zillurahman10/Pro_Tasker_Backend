# Generated by Django 5.0.6 on 2024-09-13 15:08

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='images')),
                ('category_name', models.CharField(max_length=100)),
                ('slug', models.SlugField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Portfolio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('description', models.TextField(max_length=500)),
                ('image', models.CharField(default='', max_length=500)),
                ('link', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='Skills',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('skill_name', models.CharField(max_length=100)),
                ('slug', models.SlugField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Freelancer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.CharField(default='', max_length=500)),
                ('descriptions', models.CharField(blank=True, default=None, max_length=500)),
                ('rating', models.CharField(blank=True, choices=[('✩', '✩'), ('✩✩', '✩✩'), ('✩✩✩', '✩✩✩'), ('✩✩✩✩', '✩✩✩✩'), ('✩✩✩✩✩', '✩✩✩✩✩')], default=('✩', '✩'), max_length=500)),
                ('location', models.CharField(blank=True, default=None, max_length=100)),
                ('category', models.ManyToManyField(blank='true', default=None, to='freelancer.category')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('portfilio', models.ForeignKey(blank=True, default=None, on_delete=django.db.models.deletion.CASCADE, to='freelancer.portfolio')),
                ('skills', models.ManyToManyField(blank='true', default=None, to='freelancer.skills')),
            ],
        ),
    ]
