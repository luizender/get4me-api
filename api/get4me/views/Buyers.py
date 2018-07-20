from rest_framework import viewsets, permissions
from get4me.models import BuyersModel
from get4me.serializers import BuyersSerializer

class BuyersView(viewsets.ModelViewSet):

    queryset = BuyersModel.objects.all()
    serializer_class = BuyersSerializer

    def get_queryset(self):
        if self.request.user.is_staff:
            return BuyersModel.objects.all()
        return BuyersModel.objects.filter(user__username=self.request.user)

    def get_permissions(self):
        if self.action == 'list':
            self.permission_classes = [permissions.IsAuthenticated, permissions.IsAdminUser]
        elif self.action == 'create':
            self.permission_classes = [permissions.AllowAny]

        return super(BuyersView, self).get_permissions()
