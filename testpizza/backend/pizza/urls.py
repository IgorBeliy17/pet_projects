from django.urls import path
from . import views


app_name = 'pizza'

urlpatterns = [
    path('', views.index, name='home'),
    path('pizza/<slug>', views.pizza, name='pizza'),
    path('create_pizza', views.create_pizza, name='create_pizza'),
    path('search/', views.SearchResultView.as_view(), name='search_result'),
]