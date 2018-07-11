from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.contrib.auth.validators import UnicodeUsernameValidator

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = get_user_model()
        fields = (
            'first_name', 'last_name', 'username', 'password', 'email'
        )
        extra_kwargs = {
            'username': {
                'validators': [UnicodeUsernameValidator()]
            },
            'password': {
                'write_only': True
            }
        }


class ModelHasUserSerializer(serializers.ModelSerializer):

    user = UserSerializer(required=True)

    def create(self, validated_data):
        user = get_user_model().objects.create_user(**validated_data.pop('user'))
        instance = self.Meta.model.objects.create(user=user, **validated_data)
        return instance

    def update(self, instance, validated_data):
        user_data = validated_data.pop('user')
        if user_data:
            instance.user.first_name = user_data['first_name']
            instance.user.last_name = user_data['last_name']
            instance.user.username = user_data['username']
            instance.user.email = user_data['email']
            instance.user.set_password(user_data['password'])
            instance.user.save()

        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()

        return instance
