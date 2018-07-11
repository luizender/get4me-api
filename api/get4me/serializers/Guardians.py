from rest_framework import serializers
from .Users import ModelHasUserSerializer
from get4me.models import GuardiansModel

class GuardiansSerializer(ModelHasUserSerializer):
    
    class Meta:
        
        model = GuardiansModel
        fields = '__all__'
