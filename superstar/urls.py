from django.urls import path
from .views import display,new
urlpatterns = [
    path('display/',display,name='display'),
    path('new/',new,name='new')
]