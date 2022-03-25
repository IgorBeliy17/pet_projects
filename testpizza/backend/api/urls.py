from .views import PizzaViewSet
from rest_framework import routers

pizza_router = routers.DefaultRouter()
pizza_router.register('pizza', PizzaViewSet)

urlpatterns = []
urlpatterns += pizza_router.urls
