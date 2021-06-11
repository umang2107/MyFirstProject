from django.db import models

# Create your models here.
class contact(models.Model):
    Email=models.CharField(max_length=122)
    Name=models.CharField(max_length=122)
    Password=models.CharField(max_length=16)
    Mobileno=models.CharField(max_length=10)
    date=models.DateField()