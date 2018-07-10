from drf_writable_nested import WritableNestedModelSerializer
from .Users import UserSerializer
from ..models import BuyersModel

class BuyersSerializer(WritableNestedModelSerializer):

    user = UserSerializer()
    
    class Meta:
        
        model = BuyersModel
        fields = (
            'user', 'address', 'district', 'state',
            'code', 'country', 'phone'
        )
