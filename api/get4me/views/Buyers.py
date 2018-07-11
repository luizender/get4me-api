from rest_framework import viewsets
from get4me.models import BuyersModel
from get4me.serializers import BuyersSerializer

class BuyersView(viewsets.ModelViewSet):

    queryset = BuyersModel.objects.all()
    serializer_class = BuyersSerializer
