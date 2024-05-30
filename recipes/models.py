# models.py
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils import timezone

class Category(models.Model):
    name = models.CharField(max_length=255)
    
    def __str__(self):
        return str(self.name)
    
    def get_absolute_url(self):
        return reverse("home")

class Recipe(models.Model):
    
    CATEGORY_CHOICES = [
        ('jawa', 'Jawa'),
        ('kalimantan', 'Kalimantan'),
        ('papua', 'Papua'),
        ('sulawesi', 'Sulawesi'),
        ('sumatra', 'Sumatra'),
    ]
    
    title = models.CharField(max_length=100)
    description = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.CharField(max_length=255, default='uncategorized', choices=CATEGORY_CHOICES)
    created_at = models.DateTimeField(default=timezone.now)
    updated_at = models.DateTimeField(auto_now=True)
    recipe_image = models.ImageField(upload_to='images/')
    
    def get_absolute_url(self):
        return reverse("recipes-detail", kwargs={"pk": self.pk})
    
    def __str__(self):
        return str(self.title)
