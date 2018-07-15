from django.db import models
from django.contrib.auth import get_user_model

class BuyersModel(models.Model):

    user = models.OneToOneField(get_user_model(), on_delete=models.CASCADE, default=None)
    address = models.CharField(max_length=255)
    district = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    postcode = models.CharField(max_length=255)
    country = models.CharField(max_length=255)
    phone = models.CharField(max_length=15)

    class Meta:
        db_table = 'buyers'

    def delete(self, *args, **kwargs):
        if self.user:
            self.user.delete()

        return super(BuyersModel, self).delete(*args, **kwargs)
