from django.shortcuts import render
from datetime import datetime
from superstar.models import City

# Create your views here.
def display(request):
    greet="Good Morning" if datetime.now().hour<12 else "Good Evening"
    cities = City.objects.all()
    context = {
        'time':datetime.now(),
        'greet':greet,
        'cities':cities
    }
    return render(request,'display.html',context)