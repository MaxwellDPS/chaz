from rest_framework import serializers
from the_thing.models import AThing

# pylint: disable = missing-class-docstring
class AThingSerializer(serializers.ModelSerializer):
    class Meta:
        model = AThing
        fields = [
            'uuid'
        ]
