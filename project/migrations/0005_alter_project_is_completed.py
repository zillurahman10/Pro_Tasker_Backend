# Generated by Django 5.0.6 on 2024-09-10 06:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0004_alter_project_attachments'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='is_completed',
            field=models.BooleanField(default=False),
        ),
    ]
