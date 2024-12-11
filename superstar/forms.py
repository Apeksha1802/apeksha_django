from django import forms

class SumForm(forms.Form):
    n1=forms.IntegerField(label="First Number", required=True)
    n2=forms.IntegerField(label="Second Number", required=True)
    