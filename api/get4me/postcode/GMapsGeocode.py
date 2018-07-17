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

    def _get_latitude_longitude(self):
        if self.response and len(self.response) > 0:
            for data in self.response:
                if data['geometry'] and 'location' in data['geometry']:
                    return data['geometry']['location']
        return None

    def geocode(self):
        gmaps = Client(key=settings.GMAPS_API_KEY)
        self.response = gmaps.geocode(address=self.full_address)

    def get_latitude_longitude(self):
        if not self.response:
            self.geocode()
        return self._get_latitude_longitude()

    def get_place_id(self):
        if not self.response:
            self.geocode()
        return self._get_place_id()
