from googlemaps import Client
from django.conf import settings

class GMapsDistance(object):

    def __init__(self, full_address):
        self.gmaps = None
        self.origin = full_address
        self.destin = []
        self._destin_dict = dict()

    def _get_elements(self, data):
        if data and 'rows' in data:
            row = data['rows'][0]
            if row and 'elements' in row:
                return row['elements']
        return None

    def _build_data_with_postcode(self, response):
        data = dict()
        elements = self._get_elements(response)
        for id, full_address in self._destin_dict.items():
            index = self.destin.index(full_address)
            data[id] = elements[index]
        return data

    def add_destination(self, id, full_address):
        if not full_address in self.destin:
            self._destin_dict[id] = full_address
            self.destin.append(full_address)
    
    def connect(self):
        self.gmaps = Client(key=settings.GMAPS_API_KEY)
    
    def get_distance_duration(self):
        gmaps = Client(key=settings.GMAPS_API_KEY)
        response = gmaps.distance_matrix(self.origin, self.destin)
        return self._build_data_with_postcode(response)

