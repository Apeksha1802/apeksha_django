from django.contrib import admin
from superstar.models import City, Country, State, Employee
#from django.db.migrations.recorder import MigrationRecorder
# Register your models here.

#admin.site.register(MigrationRecorder.Migration)

class EmployeeAdmin(admin.ModelAdmin):
    def get_state_object(self,obj):
        return obj.city.state.name if obj.city else None
    get_state_object.short_description = 'State'
    list_display=("id","name","mobile","address","city","get_state_object")
    search_fields=['name','mobile']
admin.site.register(Employee,EmployeeAdmin)

class StateAdmin(admin.ModelAdmin):
    list_display=("id","name")
admin.site.register(State,StateAdmin)

class CityAdmin(admin.ModelAdmin):
    list_display=("id","name","state")
admin.site.register(City,CityAdmin)
#admin.site.register(Country)

class CountryAdmin(admin.ModelAdmin):
    list_display=("id","name","population","continent")
    search_fields=['name','continent']
admin.site.register(Country,CountryAdmin)

# class StateAdmin(admin.ModelAdmin):
#     list_display=("id","name","population","capital")
# admin.site.register(State,StateAdmin)