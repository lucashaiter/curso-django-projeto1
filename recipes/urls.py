from django.urls import path
from recipes.views import home_view, contato_view, sobre_view

urlpatterns = [
    path('', home_view), 
    path('contato/', contato_view),
    path('sobre/', sobre_view)
]