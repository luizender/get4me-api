from get4me.models import GuardiansModel
from get4me.serializers import UserSerializer
from .inheritances import HasAddressSerializer, HasUserSerializer

class GuardiansSerializer(HasAddressSerializer, HasUserSerializer):

    user = UserSerializer(required=True)
    
    class Meta:
        
        model = GuardiansModel
        fields = '__all__'
        read_only_fields = ('latitude', 'longitude')
