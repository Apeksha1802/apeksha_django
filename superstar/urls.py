from django.urls import path
from .views import display,listview,calc_sum,add_state,create_employee,signup,CustomLoginView,CustomLogoutView,logged_in_users
from .views import state_list_create_view,calculator_view

urlpatterns = [
    path('display/',display,name='display'),
    path('listview/',listview,name='listview'),
    path('calculatesum/',calc_sum,name='calc_sum'),
    path('addstate/',add_state,name='add_state'),
    path('createemployee/',create_employee,name='create_employee'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', CustomLogoutView.as_view(), name='logout'),
    path('signup/', signup, name='signup'),
    path('loggedinusers/',logged_in_users,name='logged_in_users'),
    path('states/',state_list_create_view,name='state_list_create_view'),
    path('calculator/',calculator_view,name='ccalculator_view'),
]