from rest_framework import serializers
from .Users import ModelHasUserSerializer
from get4me.models import GuardiansModel
from get4me.postcode import GMapsGeocode

class GuardiansSerializer(ModelHasUserSerializer):
    
    class Meta:
        
        model = GuardiansModel
        fields = '__all__'
        read_only_fields = ('latitude', 'longitude')

    def _was_changed_address(self, instance, validated_data):
        return (instance.address != validated_data['address'] or
            instance.neighborhood != validated_data['neighborhood'] or
            instance.city != validated_data['city'] or
            instance.state != validated_data['state'] or
            instance.postcode != validated_data['postcode'] or
            instance.country != validated_data['country'])

    def _set_latitude_longitude(self, instance):
        gmaps = GMapsGeocode(instance.full_address())
        response = gmaps.get_latitude_longitude()
        if not response:
            raise serializers.ValidationError(detail='Invalid location', code='full_address')

        instance.latitude = response['lat']
        instance.longitude = response['lng']
        instance.save()

    def create(self, validated_data):
        instance = super(GuardiansSerializer, self).create(validated_data)
        self._set_latitude_longitude(instance)
        return instance

    def update(self, instance, validated_data):
        if self._was_changed_address(instance, validated_data):
            self._set_latitude_longitude(instance)

        return super(GuardiansSerializer, self).update(instance, validated_data)
