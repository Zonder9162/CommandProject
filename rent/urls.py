from xml.etree.ElementInclude import include
from django.urls import path, include

from .views import HouseViewSet, RentViewSet
from rest_framework.routers import SimpleRouter

router = SimpleRouter()

router.register('houses', HouseViewSet, basename='houses')
router.register('rents', RentViewSet, basename='rents')
urlpatterns = [
    path('', include(router.urls)),
]