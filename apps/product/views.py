from rest_framework import generics
from .models import Place, Storehouse
from .serializers import PlaceListSerializer, StorehouseSerializer


class PlaceListAPIView(generics.ListAPIView):
    #  http://127.0.0.1:8000/product/place_list/
    queryset = Place.objects.all()
    serializer_class = PlaceListSerializer


class StorehouseListAPIView(generics.ListAPIView):
    #  http://127.0.0.1:8000/product/place/place_id/storehouse/
    queryset = Storehouse.objects.all()
    serializer_class = StorehouseSerializer

    def get_queryset(self):  # --> filtering Storehouse data by place
        qs = super().get_queryset()
        place_id = self.kwargs.get('place_id')
        return qs.filter(place_id=place_id)
