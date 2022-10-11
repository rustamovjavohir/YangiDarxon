from rest_framework import serializers
from drf_extra_fields.fields import Base64ImageField

from advertising.models import Advertising


class AdvertisingSerializer(serializers.ModelSerializer):
    image = Base64ImageField(required=False)

    class Meta:
        model = Advertising
        fields = "__all__"
        extra_kwargs = {
            'is_deleted': {'write_only': True},
        }

    def create(self, validated_data):
        if validated_data.get('image'):
            image = validated_data.pop('image')
        else:
            image = ''

        return Advertising.objects.create(image=image, **validated_data)
