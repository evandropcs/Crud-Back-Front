from django.urls import path
from . import views

urlpatterns = [
    # path('', views.homePage, name='homePage'),
    path('api/tarefas', views.home, name='home'),
]
