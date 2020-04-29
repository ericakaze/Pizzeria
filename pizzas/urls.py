"""defines URL patterns for pizzas."""
from django.urls import path
from . import views
app_name='pizzas'
urlpatterns=[path('', views.index, name='index'),
#page that shows all Pizzas
path('pizzas/', views.pizzas, name='pizzas'),
path('pizzas/<int:topic_id>/',views.pizza, name='pizza'),
]

