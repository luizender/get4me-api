from googlemaps import Client
from django.conf import settings

class GMapsGeocode(object):

    def __init__(self, full_address):
        self.full_address = full_address
        self.response = None

    def _get_place_id(self):
        if self.response and len(self.response) > 0:
            for data in self.response:
                if data['place_id']:
                    return 'place_id:' + data['place_id']
        return None

    def get_place_id(self):
        if not self.response:
            gmaps = Client(key=settings.GMAPS_API_KEY)
            self.response = gmaps.geocode(self.full_address)
        return self._get_place_id()
