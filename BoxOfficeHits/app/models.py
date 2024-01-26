from django.db import models

# Create your models here.

class Subscription(models.Model):
    Name=models.CharField(max_length=30)
    Movie=models.CharField(max_length=60)
    Actor=models.CharField(max_length=50)
    Actress=models.CharField(max_length=50)
    Email=models.EmailField(max_length=50,null=True)
    Genre=models.CharField(max_length=60)
    Payment=models.CharField(max_length=60)
    