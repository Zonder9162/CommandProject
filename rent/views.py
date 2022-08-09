from rest_framework.viewsets import GenericViewSet
from rest_framework import mixins
from .models import House, Rent
from .serializers import HouseSerializer, RentSerializer
from rest_framework.viewsets import ModelViewSet

class HouseViewSet(ModelViewSet, GenericViewSet):
    queryset = House.objects.all()
    serializer_class = HouseSerializer

class RentViewSet(mixins.CreateModelMixin, mixins.DestroyModelMixin, GenericViewSet):
    queryset = Rent.objects.all()
    serializer_class = RentSerializer