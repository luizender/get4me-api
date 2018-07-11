from .Users import ModelHasUserSerializer
from get4me.models import BuyersModel

class BuyersSerializer(ModelHasUserSerializer):

    class Meta:
        
        model = BuyersModel
        fields = '__all__'
