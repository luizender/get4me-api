from rest_framework import serializers
from ..models import GuardiansModel

class GuardiansSerializer(serializers.ModelSerializer):
    
    class Meta:
        
        model = GuardiansModel
        fields = '__all__'
