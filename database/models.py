from django.db import models

class enquiry(models.Model):
    name=models.CharField(max_length=50)
    email=models.CharField(max_length=50)
    phoneno=models.CharField(max_length=50)
    website=models.CharField(max_length=50)
    message=models.TextField()
# Create your models here.
