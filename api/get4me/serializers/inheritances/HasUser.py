from rest_framework import serializers
from django.contrib.auth import get_user_model

class HasUserSerializer(serializers.ModelSerializer):

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