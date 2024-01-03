from django.db import models
from django.contrib.auth.models import User
# Create your models here.







class Books(models.Model):
    name = models.CharField(max_length=200)
    autor = models.CharField(max_length=200)
    price = models.PositiveIntegerField()
    quatity  = models.IntegerField()
    



