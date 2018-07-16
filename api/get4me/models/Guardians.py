from django.db import models
from django.contrib.auth import get_user_model

class GuardiansManager(models.Manager):

    def filter_by_info(self, state, city, district):
        objects = GuardiansModel.objects.filter(state=state, city=city, district=district)
        if len(objects) > 0:
            return objects

        objects = GuardiansModel.objects.filter(state=state, city=city)
        if len(objects) > 0:
            return objects

        objects = GuardiansModel.objects.filter(state=state)
        if len(objects) > 0:
            return objects

        return GuardiansModel.objects.all()

class GuardiansModel(models.Model):

    objects = GuardiansManager()

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

    class Meta:
        db_table = 'guardians'

    def full_name(self):
        if self.user:
            return self.user.first_name + ' ' + self.user.last_name
        return ''

    def full_address(self):
        return '%s - %s, %s - %s, %s, %s' % (
            self.address, self.district, self.city,
            self.state, self.postcode, self.country
        )
