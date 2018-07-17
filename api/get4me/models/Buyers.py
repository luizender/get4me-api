from django.db import models
from django.contrib.auth import get_user_model

class BuyersModel(models.Model):

    user = models.OneToOneField(get_user_model(), on_delete=models.CASCADE, default=None)
    address = models.CharField(max_length=255)
    neighborhood = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    postcode = models.CharField(max_length=255)
    country = models.CharField(max_length=255)
    phone = models.CharField(max_length=15)
    latitude = models.FloatField(default=0)
    longitude = models.FloatField(default=0)

    class Meta:
        db_table = 'buyers'

    def full_name(self):
        if self.user:
            return self.user.first_name + ' ' + self.user.last_name
        return ''

    def full_address(self):
        return '%s - %s, %s - %s, %s, %s' % (
            self.address, self.neighborhood, self.city,
            self.state, self.postcode, self.country
        )

    def delete(self, *args, **kwargs):
        if self.user:
            self.user.delete()

        return super(BuyersModel, self).delete(*args, **kwargs)
