from django import forms
from .models import Employee

# class SumForm(forms.Form):
#     number1=forms.IntegerField(label="First Number", required=True)
#     number2=forms.IntegersField(label="Second Number", required=True)

class EmployeeForm(forms.ModelForm):
    class Meta:
        model=Employee
        fields=['name','mobile','address','city']