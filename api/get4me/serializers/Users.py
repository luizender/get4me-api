from rest_framework import serializers
from django.contrib.auth import get_user_model

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = get_user_model()
        fields = (
            'first_name', 'last_name', 'username', 'password', 'email'
        )

class ModelHasUserSerializer(serializers.ModelSerializer):

    user = UserSerializer(required=True)

    def create(self, validated_data):
        user = get_user_model().objects.create_user(**validated_data.pop('user'))
        instance = self.Meta.model.objects.create(user=user, **validated_data)
        return instance
