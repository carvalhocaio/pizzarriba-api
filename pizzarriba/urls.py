from django.urls import path, include
from rest_framework import routers
from pizzarriba.views import DishView

router = routers.DefaultRouter()
router.register(r"dishes", DishView)

urlpatterns = [
    path("", include(router.urls)),
]
