import pycep_correios

class PostCodeInformation(object):

    def __init__(self, postcode):
        self.postcode = postcode
        self.information = None

    def consult(self):
        try:
            self.information = pycep_correios.consultar_cep(self.postcode)
        except Exception as ex:
            self.information = None

    def get_address(self):
        if self.information:
            return self.information['end']
        return None

    def get_city(self):
        if self.information:
            return self.information['cidade']
        return None
    
    def get_state(self):
        if self.information:
            return self.information['uf']
        return None

    def get_district(self):
        if self.information:
            return self.information['bairro']
        return None