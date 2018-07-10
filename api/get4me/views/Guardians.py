from rest_framework import viewsets
from ..models import GuardiansModel
from ..serializers import GuardiansSerializer

class GuardiansView(viewsets.ModelViewSet):

    queryset = GuardiansModel.objects.all()
    serializer_class = GuardiansSerializer