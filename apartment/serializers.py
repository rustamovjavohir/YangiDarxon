from rest_framework import serializers
from apartment.models import Apartment, Filial
from drf_extra_fields.fields import Base64ImageField


class ApartmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Apartment
        depth = 1
        fields = '__all__'
        extra_kwargs = {
            'is_deleted': {'write_only': True},
        }


class FilialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Filial
        depth = 1
        fields = '__all__'
        extra_kwargs = {
            'is_deleted': {'write_only': True},
        }


class MyImageModelSerializer(serializers.ModelSerializer):
    image = Base64ImageField(required=False)
    image_2d = Base64ImageField(required=False)
    image_3d = Base64ImageField(required=False)

    class Meta:
        model = Apartment
        fields = '__all__'
        extra_kwargs = {
            'is_deleted': {'write_only': True},
        }

    def create(self, validated_data):
        if validated_data.get("image"):
            image = validated_data.pop('image')
        else:
            image = ''
        if validated_data.get("image_2d"):
            image_2d = validated_data.pop('image_2d')
        else:
            image_2d = ''
        if validated_data.get("image_3d"):
            image_3d = validated_data.pop('image_3d')
        else:
            image_3d = ''

        return Apartment.objects.create(image=image, image_2d=image_2d, image_3d=image_3d, **validated_data)
