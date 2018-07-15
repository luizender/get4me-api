from googlemaps import Client
from django.conf import settings

class GMaps(object):

    def __init__(self):
        self.gmaps = None

    def __del__(self):
        if self.gmaps:
            del self.gmaps
    
    def connect(self):
        self.gmaps = Client(key=settings.GMAPS_API_KEY)
    
    def get_distance(self, origin, destin):
        return self.gmaps.distance_matrix(origin, destin)
