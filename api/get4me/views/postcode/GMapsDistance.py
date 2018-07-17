from googlemaps import Client
from django.conf import settings

class GMapsDistance(object):

    def __init__(self, origin):
        self.place_id = None
        self.destin = []
        self._destin_dict = dict()
        self.origin = origin

    def _get_elements_from_response(self, response):
        if response and 'rows' in response:
            row = response['rows'][0]
            if row and 'elements' in row:
                return row['elements']
        return None

    def _build_data_with_postcode(self, response):
        data = dict()
        elements = self._get_elements_from_response(response)
        for id, destin in self._destin_dict.items():
            index = self.destin.index(destin)
            data[id] = elements[index]
        return data

    def add_destination(self, id, destin):
        if not destin in self.destin:
            self._destin_dict[id] = destin
            self.destin.append(destin)
    
    def get_distance_duration(self):
        gmaps = Client(key=settings.GMAPS_API_KEY)
        response = gmaps.distance_matrix(self.origin, self.destin)
        return self._build_data_with_postcode(response)
