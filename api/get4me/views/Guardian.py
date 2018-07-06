from rest_framework import viewsets
from ..models import GuardianModel
from ..serializers import GuardianSerializer

class GuardianView(viewsets.ModelViewSet):

    queryset = GuardianModel.objects.all()
    serializer_class = GuardianSerializer