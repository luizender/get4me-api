from .Users import ModelHasUserSerializer
from ..models import BuyersModel

class BuyersSerializer(ModelHasUserSerializer):

    class Meta:
        
        model = BuyersModel
        fields = (
            'id', 'user', 'address', 'district',
            'state', 'code', 'country', 'phone'
        )
