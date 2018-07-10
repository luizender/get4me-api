from rest_framework import viewsets
from ..models import BuyersModel
from ..serializers import BuyersSerializer

class BuyersView(viewsets.ModelViewSet):

    queryset = BuyersModel.objects.all()
    serializer_class = BuyersSerializer
