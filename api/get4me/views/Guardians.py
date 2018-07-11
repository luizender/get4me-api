from rest_framework import viewsets
from get4me.models import GuardiansModel
from get4me.serializers import GuardiansSerializer

class GuardiansView(viewsets.ModelViewSet):

    queryset = GuardiansModel.objects.all()
    serializer_class = GuardiansSerializer