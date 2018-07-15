from rest_framework import viewsets, generics, status
from rest_framework.response import Response
from get4me.serializers import PostcodeSerializer
from get4me.models import GuardiansModel

class PostcodeView(viewsets.ReadOnlyModelViewSet):

    queryset = GuardiansModel.objects.all()
    serializer_class = PostcodeSerializer

    def get_queryset(self):
        postcode = self.request.GET.get('postcode', None)
        if postcode:
            # TODO: Add the logic to get the state of postcode to filter the guardians list
            return GuardiansModel.objects.filter()
        return GuardiansModel.objects.all()

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())

        postcode = self.request.GET.get('postcode', None)
        if postcode:
            for guardian in queryset:
                # TODO: Add the logic to consume the Google Distance Matrix API
                # to set distance and duration of guardian data.
                guardian.distance = 0
                guardian.duration = 0

        serializer = self.get_serializer(queryset, many=True)

        return Response(serializer.data)