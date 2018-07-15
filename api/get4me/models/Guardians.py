from django.db import models
from django.contrib.auth import get_user_model

class GuardiansModel(models.Model):

    user = models.OneToOneField(get_user_model(), on_delete=models.CASCADE, default=None)
    address = models.CharField(max_length=255)
    district = models.CharField(max_length=255)
    city = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    postcode = models.CharField(max_length=255)
    country = models.CharField(max_length=255)
    phone = models.CharField(max_length=15)
    start_work = models.TimeField()
    end_work = models.TimeField()
    distance = None
    duration = None

    class Meta:
        db_table = 'guardians'

    def name(self):
        if self.user:
            return self.user.first_name + ' ' + self.user.last_name
        return ''