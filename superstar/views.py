from django.shortcuts import render
from datetime import datetime
from superstar.models import City, Country, State, Employee

# Create your views here.
def display(request):
    cities = City.objects.all()
    countries=Country.objects.all()
    states=State.objects.all()
    employees=Employee.objects.all()
    context = {
        'time':datetime.now(),
        'greet':greet,
        'cities':cities,
        'countries':countries,
        'states':states,
        'employees':employees,
    }
    return render(request,'display.html',context)

def new(request):
    greet="Good Morning..." if datetime.now().hour<12 else "Good Evening..."
    context={
        'greet':greet
    }
    
    return render(request,'new.html',context)