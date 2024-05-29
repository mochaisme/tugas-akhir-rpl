# Generated by Django 4.2.13 on 2024-05-14 09:49

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('recipes', '0002_recipe_recipe_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='recipe',
            name='favourite',
            field=models.ManyToManyField(blank=True, related_name='favourite', to=settings.AUTH_USER_MODEL),
        ),
    ]
