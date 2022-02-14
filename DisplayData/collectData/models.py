from email.policy import default
from django.db import models

# Create your models here.
class MyData(models.Model):
    temperature = models.CharField(max_length=100, default=0)
    moisture = models.CharField(max_length=100, default=0)
    humidity = models.CharField(max_length=100, default=0)
    pump = models.BooleanField(default=False)
