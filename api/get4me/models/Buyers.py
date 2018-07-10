from django.db import models
from django.contrib.auth import get_user_model

class BuyersModel(models.Model):

    user = models.OneToOneField(get_user_model(), on_delete=models.CASCADE, default=None)
    address = models.CharField(max_length=255)
    district = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    code = models.CharField(max_length=255)
    country = models.CharField(max_length=255)
    phone = models.CharField(max_length=15)

    class Meta:
        db_table = 'buyers'

