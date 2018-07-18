from rest_framework.validators import UniqueValidator
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
