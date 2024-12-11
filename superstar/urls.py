from django.urls import path
from .views import display,listview,calc_sum
urlpatterns = [
    path('display/',display,name='display'),
    path('listview/',listview,name='listview'),
    path('calculatesum/',calc_sum,name='calc_sum'),
]