from django.urls import path
from .views import PlaceListAPIView, StorehouseListAPIView

urlpatterns = [
    path('place_list/', PlaceListAPIView.as_view()),
    path('place/<int:place_id>/storehouse/', StorehouseListAPIView.as_view()),
]
