from django.conf import settings
from django.db import models


# Create your models here.
class Profile(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    phone = models.CharField(max_length=14, db_index=True)
    address = models.CharField(max_length=200)

