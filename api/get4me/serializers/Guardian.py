from rest_framework import serializers
from ..models import GuardianModel

class GuardianSerializer(serializers.ModelSerializer):
    
    class Meta:
        
        model = GuardianModel
        fields = '__all__'
