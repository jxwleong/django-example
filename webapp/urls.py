from django.urls import path 
from . import views, views2

urlpatterns = [
    path('hello/', views.say_hello),
    #path('', views.index, name='index'),
    path('', views2.index, name='index'),
]