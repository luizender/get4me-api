from rest_framework import serializers

class PostcodeSerializer(serializers.Serializer):

    full_name = serializers.CharField(read_only=True)
    address = serializers.CharField(read_only=True)
    district = serializers.CharField(read_only=True)
    city = serializers.CharField(read_only=True)
    state = serializers.CharField(read_only=True)
    country = serializers.CharField(read_only=True)
    postcode = serializers.CharField(read_only=True)
    phone = serializers.CharField(read_only=True)
    start_work = serializers.TimeField(read_only=True)
    end_work = serializers.TimeField(read_only=True)
    distance = serializers.SerializerMethodField()
    duration = serializers.SerializerMethodField()
    
    def __init__(self, *args, **kwargs):
        self.gmaps_data = kwargs.pop('gmaps_data', None)
        super(PostcodeSerializer, self).__init__(*args, **kwargs)

    def get_distance(self, obj):
        if self.gmaps_data and self.gmaps_data[obj.id]:
            data = self.gmaps_data[obj.id]
            if data and 'distance' in data:
                return data['distance']['value']
        return 0

    def get_duration(self, obj):
        if self.gmaps_data and self.gmaps_data[obj.id]:
            data = self.gmaps_data[obj.id]
            if data and 'distance' in data:
                return data['duration']['value']
        return 0
