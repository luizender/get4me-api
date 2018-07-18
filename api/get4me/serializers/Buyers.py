from get4me.models import BuyersModel
from get4me.serializers import UserSerializer
from .inheritances import HasAddressSerializer, HasUserSerializer

class BuyersSerializer(HasAddressSerializer, HasUserSerializer):

    user = UserSerializer(required=True)

    class Meta:
        
        model = BuyersModel
        fields = '__all__'
        read_only_fields = ('latitude', 'longitude')
