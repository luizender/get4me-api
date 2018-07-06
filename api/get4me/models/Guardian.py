from django.db import models

class GuardianModel(models.Model):
    
    name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    district = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    code = models.CharField(max_length=255)
    country = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    start_work = models.TimeField()
    end_work = models.TimeField()