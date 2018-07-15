from rest_framework import serializers

class PostcodeSerializer(serializers.Serializer):
    name = serializers.CharField(read_only=True)
    address = serializers.CharField(read_only=True)
    district = serializers.CharField(read_only=True)
    postcode = serializers.CharField(read_only=True)
    state = serializers.CharField(read_only=True)
    country = serializers.CharField(read_only=True)
    phone = serializers.CharField(read_only=True)
    start_work = serializers.TimeField(read_only=True)
    end_work = serializers.TimeField(read_only=True)
    distance = serializers.IntegerField(read_only=True)
    duration = serializers.IntegerField(read_only=True)


