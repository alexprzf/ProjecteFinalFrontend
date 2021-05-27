from django.db import models

# Create your models here.
class Dpor(models.Model):
    user = models.CharField(max_length=100)
    file = models.FileField(upload_to='uploads')
    path = models.CharField(max_length=100)
    isUpdated = models.BooleanField(default=True)
