from django.db import models
from tinymce.models import HTMLField
class news(models.Model):
    first_title=models.CharField(max_length=50)
    icon=models.CharField(max_length=50)
    service_des=HTMLField()
# Create your models here.
