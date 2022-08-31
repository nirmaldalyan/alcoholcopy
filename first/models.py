from django.db import models
class first(models.Model):
    first_title=models.CharField(max_length=50)
    icon=models.CharField(max_length=50)
    service_des=models.TextField()

# Create your models here.
