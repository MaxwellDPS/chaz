from the_thing.models import AThing
from the_thing.serializers import AThingSerializer

from rest_framework import generics
from rest_framework.pagination import LimitOffsetPagination


class List(generics.ListCreateAPIView, LimitOffsetPagination):
    """
    List / Create A thing ViewSet
    """
    queryset = AThing.objects.all()
    serializer_class = AThingSerializer

class View(generics.RetrieveUpdateDestroyAPIView, LimitOffsetPagination):
    """
    List / Create A thing ViewSet
    """
    queryset = AThing.objects.all()
    serializer_class = AThingSerializer
