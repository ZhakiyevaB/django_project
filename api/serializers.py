from rest_framework import serializers
from .models import Item, Location


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = '__all__'  # Или перечислите поля, которые вы хотите включить в сериализацию

class LocationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Location  # Указываем модель Location, а не Location()
        fields = '__all__'  # Используем '__all__' для указания всех полей модел