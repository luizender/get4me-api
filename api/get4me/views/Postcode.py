from rest_framework import viewsets, generics, status
from rest_framework.response import Response
from get4me.serializers import PostcodeSerializer
from get4me.models import GuardiansModel
from .postcode import PostCodeInformation, GMapsDistance

class PostcodeView(viewsets.ReadOnlyModelViewSet):

    queryset = GuardiansModel.objects.all()
    serializer_class = PostcodeSerializer

    def get_queryset(self):
        postcode = self.request.GET.get('postcode', None)
        if postcode:
            pcInfo = PostCodeInformation(postcode)
            pcInfo.consult()

            return GuardiansModel.objects.filter_by_info(
                pcInfo.get_state(), pcInfo.get_city(), pcInfo.get_district()
            )

        return GuardiansModel.objects.all()

    def list(self, request, *args, **kwargs):
        gmaps_data = None
        queryset = self.filter_queryset(self.get_queryset())

        postcode = self.request.GET.get('postcode', None)
        if postcode:
            gmaps = GMapsDistance(postcode)
            for guardian in queryset:
                gmaps.add_destination(guardian.postcode)
            gmaps_data = gmaps.get_distance_duration()

        serializer = self.get_serializer(queryset, gmaps_data=gmaps_data, many=True)

        return Response(serializer.data)