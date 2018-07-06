from rest_framework import serializers
from ..models import BuyersModel

class BuyersSerializer(serializers.ModelSerializer):
    
    class Meta:
        
        model = BuyersModel
        fields = '__all__'
