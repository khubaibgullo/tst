from django.db import models

# Create your models here.

class Gapp(models.Model):
    path = models.TextField(null=True)
    timestamp = models.DateTimeField(auto_now_add=True)