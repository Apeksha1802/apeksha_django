from django.shortcuts import render
from datetime import datetime
from superstar.models import City, Country, State, Employee, EmpID
from .forms import EmployeeForm
from django.http import HttpResponse

from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.forms import UserCreationForm
from django.contrib.sessions.models import Session
from django.contrib.auth.models import User 

from rest_framework.decorators import api_view

from rest_framework.response import Response

from rest_framework import status

from .models import State

from superstar.serializers import StateSerializer

from django.http import JsonResponse

from rest_framework.decorators import api_view

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

def add_state(request):
    if request.method=="POST":
        state_name=request.POST.get("state_name")
        if state_name:
            if State.objects.filter(name__iexact=state_name).exists():
                return HttpResponse(f"State '{state_name}' already exists in database.")
            else: 
                State.objects.create(name=state_name)
                return HttpResponse(f"State '{state_name}' added successfully")
    else:
        return render(request,'add_state.html')

def emp_id_creation():
    last_emp_id=EmpID.objects.all().order_by('id').last()
    if last_emp_id:
        last_id=int(last_emp_id.EMP_ID.split('_')[1])
        emp_id=f'F_{last_id+1:04d}'
    else:
        emp_id='F_0001'
    return emp_id

def create_employee(request):
    if request.method=='POST':
        form=EmployeeForm(request.POST)
        if form.is_valid():
            employee=form.save()
            emp_id=emp_id_creation()
            emp_id_record=EmpID.objects.create(employee=employee,EMP_ID=emp_id)

            context={
                'form':form,
                'employee':employee,
                'emp_id':emp_id,
            }
        return render(request,'employee_form.html',context)
    else:
        form=EmployeeForm()
        context={
            'form':form,
        }
    return render(request,'employee_form.html',context)

class CustomLoginView(LoginView):
    template_name = 'login.html'

class CustomLogoutView(LogoutView):
    next_page = '/calculatesum' 

@login_required
def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = UserCreationForm()
    return render(request, 'signup.html', {'form': form})

def logged_in_users(request):
    sessions=Session.objects.filter(expire_date__gte=datetime.now())
    user_ids=[]
    for session in sessions:
        data=session.get_decoded()
        if '_auth_user_id' in data:
            user_ids.append(data['_auth_user_id'])
    users=User.objects.filter(id__in=user_ids)
    return render(request,'logged_in_users.html',{'users':users})

@api_view(['GET', 'POST'])
def state_list_create_view(request):
    if request.method == 'GET':
        states = State.objects.all()
        serializer = StateSerializer(states, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'POST':
        serializer = StateSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def calculator_view(request):
  try:
    num1 = float(request.data.get('num1'))
    num2 = float(request.data.get('num2'))
    operation_type = request.data.get('type', '').lower()
    if operation_type == 'add':
      result = num1 + num2
    elif operation_type == 'sub':
      result = num1 - num2
    elif operation_type == 'mul':
      result = num1 * num2
    elif operation_type == 'div':
      if num2 == 0:
        return JsonResponse({"error": "Division by zero is not allowed"}, status=400)
      result = num1 / num2
    else:
      return JsonResponse({"error": "Invalid operation type. Use 'add', 'sub', 'mul', or 'div'."}, status=400)
    return JsonResponse({"result": result}, status=200)
  
  except ValueError:
    return JsonResponse({"error": "Invalid input. Please provide numbers for 'num1' and 'num2'."}, status=400)

  except Exception as e:
    return JsonResponse({"error": str(e)}, status=400)

