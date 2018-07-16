from googlemaps import Client
from django.conf import settings

class GMapsDistance(object):

    def __init__(self, postcode):
        self.gmaps = None
        self.origin = postcode
        self.destin = []

    def _get_elements(self, data):
        if data and 'rows' in data:
            row = data['rows'][0]
            if row and 'elements' in row:
                return row['elements']
        return None

    def _build_data_with_postcode(self, response):
        data = dict()
        elements = self._get_elements(response)
        for ps in self.destin:
            index = self.destin.index(ps)
            data[ps] = elements[index]
        return data

    def add_destination(self, postcode):
        self.destin.append(postcode)

    def del_destination(self, postcode):
        if postcode in self.destin:
            self.destin.remove(postcode)
    
    def connect(self):
        self.gmaps = Client(key=settings.GMAPS_API_KEY)
    
    def get_distance_duration(self):
        gmaps = Client(key=settings.GMAPS_API_KEY)
        response = gmaps.distance_matrix(self.origin, self.destin)
        return self._build_data_with_postcode(response)

