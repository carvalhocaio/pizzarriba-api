from rest_framework import viewsets
from pizzarriba.models import Dish
from pizzarriba.serializers import DishSerializer


class DishView(viewsets.ModelViewSet):
    queryset = Dish.objects.all()
    serializer_class = DishSerializer
