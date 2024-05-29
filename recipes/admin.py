from django.contrib import admin
from . import models
from .models import Category

# Register your models here.
admin.site.register(models.Recipe)
admin.site.register(Category)