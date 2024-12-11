from django.urls import path
from .views import display,listview,calc_sum,add_state,create_employee,signup,CustomLoginView,CustomLogoutView
urlpatterns = [
    path('display/',display,name='display'),
    path('listview/',listview,name='listview'),
    path('calculatesum/',calc_sum,name='calc_sum'),
    path('addstate/',add_state,name='add_state'),
    path('createemployee/',create_employee,name='create_employee'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', CustomLogoutView.as_view(), name='logout'),
    path('signup/', signup, name='signup'),
]