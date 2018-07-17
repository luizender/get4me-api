from rest_framework import viewsets, generics, status
from rest_framework.response import Response
from get4me.serializers import PostcodeSerializer
from get4me.models import BuyersModel, GuardiansModel
from get4me.postcode import PostCodeInformation, GMapsDistance, GMapsGeocode

class PostcodeView(viewsets.ReadOnlyModelViewSet):

    queryset = GuardiansModel.objects.all()
    serializer_class = PostcodeSerializer

    def _build_full_address(self):
        self.address = self.request.GET.get('address', None)
        self.neighborhood = self.request.GET.get('neighborhood', None)
        self.city = self.request.GET.get('city', None)
        self.state = self.request.GET.get('state', None)
        self.postcode = self.request.GET.get('postcode', None)
        self.country = self.request.GET.get('country', None)

        if self.postcode and (not self.address or not self.neighborhood or not self.city or not self.state):
            pcInfo = PostCodeInformation(self.postcode)
            pcInfo.consult()

            self.address = pcInfo.get_address()
            self.neighborhood = pcInfo.get_neighborhood()
            self.city = pcInfo.get_city()
            self.state = pcInfo.get_state()

        full_address = '%s%s%s%s%s%s' % (
            self.address + ',' if self.address else '',
            self.neighborhood + ',' if self.neighborhood else '',
            self.city + ',' if self.city else '',
            self.state + ',' if self.state else '',
            self.postcode + ',' if self.postcode else '',
            self.country if self.country else ''
        )

        if full_address[-1:] == ',':
            return full_address[:-1]
        return full_address

    def _get_latitude_longitude(self):
        if len(self.request.GET) == 0:
            objects = BuyersModel.objects.filter(user__username=self.request.user)
            if len(objects) == 0:
                return None

            buyer = objects[0]
            self.neighborhood = buyer.neighborhood
            self.city = buyer.city
            self.state = buyer.state
            return { 'lat': buyer.latitude, 'lng': buyer.longitude }

        full_address = self._build_full_address()
        if not full_address:
            return None

        gmaps = GMapsGeocode(full_address)
        return gmaps.get_latitude_longitude()

    def get_queryset(self):
        return GuardiansModel.objects.filter_by_info(
            self.state, self.city, self.neighborhood
        )

    def list(self, request, *args, **kwargs):
        try:
            data_lat_lng = self._get_latitude_longitude()
            if not data_lat_lng:
                data = { 'message': 'Invalid address' }
                return Response(data, status=status.HTTP_400_BAD_REQUEST)

            queryset = self.filter_queryset(self.get_queryset())

            gmaps = GMapsDistance(data_lat_lng)
            for guardian in queryset:
                gmaps.add_destination(
                    guardian.id, { 'lat': guardian.latitude, 'lng': guardian.longitude }
                )
            gmaps_data = gmaps.get_distance_duration()

            serializer = self.get_serializer(queryset, gmaps_data=gmaps_data, many=True)

            return Response(serializer.data)
        except Exception as ex:
            data = { "message": str(ex) }
            return Response(data, status=status.HTTP_500_INTERNAL_SERVER_ERROR)