from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet

from api.serializers import ManufacturerSerializer, ShoeTypeSerializer, ShoeColorSerializer, ShoeSerializer
from api.models import Manufacturer, Shoe, ShoeColor, ShoeType


class ManufacturerViewSet(ModelViewSet):
    serializer_class = ManufacturerSerializer
    queryset = Manufacturer.objects.all()


class ShoeTypeViewSet(ModelViewSet):
    serializer_class = ShoeTypeSerializer
    queryset = ShoeTypeSerializer.objects.all()


class ShoeColorViewSet(ModelViewSet):
    serializer_class = ShoeColorSerializer
    queryset = ShoeColorSerializer.objects.all()


class ShoeViewSet(ModelViewSet):
    serializer_class = ShoeSerializer
    queryset = ShoeSerializer.objects.all()

