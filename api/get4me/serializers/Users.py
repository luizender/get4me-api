from rest_framework import serializers
from rest_framework.validators import UniqueValidator
from django.contrib.auth import get_user_model
from django.contrib.auth.validators import UnicodeUsernameValidator
from django.utils.translation import ugettext_lazy as _

class UserUniqueValidator(UniqueValidator):

    message = _('A user with that username already exists.')

    def set_context(self, serializer_field):
        self.field_name = serializer_field.source_attrs[-1]
        self.instance = None

        user_serializer = serializer_field.parent
        if not user_serializer:
            return

        model_serializer = user_serializer.parent
        if not model_serializer:
            return

        instance = getattr(model_serializer, 'instance', None)
        if instance:
            self.instance = getattr(instance, 'user', None)

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


class ModelHasUserSerializer(serializers.ModelSerializer):

    user = UserSerializer(required=True)


    def create(self, validated_data):
        user = get_user_model().objects.create_user(**validated_data.pop('user'))
        instance = self.Meta.model.objects.create(user=user, **validated_data)
        return instance

    def update(self, instance, validated_data):
        user_data = validated_data.pop('user')
        if user_data:
            for attr, value in user_data.items():
                if attr is 'password':
                    instance.user.set_password(value)
                    continue

                setattr(instance.user, attr, value)

            instance.user.save()

        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()

        return instance
