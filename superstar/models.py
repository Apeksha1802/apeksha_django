from django.db import models

# Create your models here.
class State(models.Model):
    name=models.CharField(max_length=50)
    # population=models.IntegerField()
    # capital=models.CharField(max_length=30)
    class Meta:
        verbose_name_plural="states"
    def __str__(self):
        return self.name

class City(models.Model):
    name=models.CharField(max_length=20)
    state=models.ForeignKey(State, on_delete=models.RESTRICT, null=True)
    pincode=models.IntegerField()
    class Meta:
        verbose_name_plural="cities"
    def __str__(self):
        return self.name

class Employee(models.Model):
    name=models.CharField(max_length=50)
    mobile=models.CharField(max_length=10)
    address=models.CharField(max_length=50)
    city=models.ForeignKey(City, on_delete=models.RESTRICT, null=True)
    class Meta:
        verbose_name_plural="employees"
    def __str__(self):
        return self.name
    
class Country(models.Model):
    name=models.CharField(max_length=50)
    population=models.IntegerField()
    continent=models.CharField(max_length=30)
    class Meta:
        verbose_name_plural="countries"
    def __str__(self):
        return self.name
    
class EmpID(models.Model):
    EMP_ID=models.CharField(max_length=10,unique=True)
    employee=models.OneToOneField(Employee,on_delete=models.RESTRICT)

    def __str__(self):
        return self.EMP_ID