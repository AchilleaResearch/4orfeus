from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class busCoordinates(models.Model):
    fname = models.CharField(max_length=100)
    file = models.FileField(upload_to='systemfiles/')
    definedby = models.ForeignKey(User, on_delete=models.CASCADE, default="", null=True)
    definedon = models.DateTimeField(auto_now_add=True)
    def __str__(self) -> str:
        return self.fname

class scID(models.Model):
    selected = models.CharField(max_length=1000)
