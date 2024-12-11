from django.shortcuts import render
from datetime import datetime
from superstar.models import City, Country, State, Employee
from .forms import SumForm

# Create your views here.
def display(request):
    greet="Good Morning" if datetime.now().hour<12 else "Good Evening"
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

def listview(request):
    employees=Employee.objects.all()
    context={
        'employee':employees,
    }
    return render(request,'listview.html',context)

def calc_sum(request):
    result=None
    if request.method=="POST":
        try:
            number1=int(request.POST.get('number1',0))
            number2=int(request.POST.get('number2',0))
            result=number1+number2
        except ValueError:
            result="Invalid Input"
        # form=SumForm(request.POST)
        # if form.is_valid():
        #     number1=form.cleaned_data['number1']
        #     number2=form.cleaned_data['number2']
        #     result=number1+number2 
    # else:
    #     form=SumForm()
    return render(request,'sum_page.html',{'result':result})