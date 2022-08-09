from rest_framework import serializers
from .models import House, Rent



class HouseSerializer(serializers.ModelSerializer):
    class Meta:
        model = House
        fields = '__all__'

    def to_representation(self, instance):
        repr = super().to_representation(instance)
        repr['rents'] = RentSerializer(instance.rents.all(), many=True).data

        return repr


class RentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rent
        fields = '__all__'