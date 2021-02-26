from django.db import models

# Create your models here.


class UserSecondary(models.Model):
    username = models.CharField(max_length=20, unique=True)
    first_name = models.CharField(max_length=50, null=True)
    last_name = models.CharField(max_length=50, null=True)
    category = models.CharField(max_length=30, default="misc")
    password_hash = models.CharField(max_length=128, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    modified_at = models.DateTimeField(auto_now=True)
