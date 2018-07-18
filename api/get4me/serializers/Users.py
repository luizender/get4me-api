from rest_framework import serializers
from django.contrib.auth import get_user_model
from django.contrib.auth.validators import UnicodeUsernameValidator
from .validators import UserUniqueValidator

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = get_user_model()
        fields = (
            'first_name', 'last_name', 'username', 'password', 'email'
        )
        extra_kwargs = {
            'username': {
                'validators': [
                    UnicodeUsernameValidator(),
                    UserUniqueValidator(queryset=get_user_model().objects.all())
                ]
            },
            'password': {
                'write_only': True
            }
        }
