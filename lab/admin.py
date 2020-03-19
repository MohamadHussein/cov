from django.contrib import admin

from lab.models import  *
from leaflet.admin import LeafletGeoAdmin
from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from import_export import resources


class TestResource(resources.ModelResource):
    class Meta:
        model = Test

class LabAdmin(LeafletGeoAdmin):
    fieldsets = (
        ('Lab Info', {'fields': ['name','manager']}),
        ('Lab location :', {'fields': ['area','address','point_type','location']})
    )


class DoctorAdmin(LeafletGeoAdmin):
    fieldsets = (
        ('Doctor Information', {
            'fields': ['user', 'Doctor_ID', 'name', 'gender','birth_date', 'phone']}),
        ('Working Labs ', {'fields': ['lab']}),
        ('Doctor location ', {'fields': ['address', 'location',]}),
    )


class PatientAdmin(admin.ModelAdmin):
     fieldsets = (
        ('Patient Information', {'fields': ['user','patient_ID','Salutation','first_name','middle_initial','middle_name','surname','gender','birth_date','phone',]}),
        ('Patient location ', {'fields': ['country', 'state','address']}),
        ('Lab ', {'fields': ['lab']}),
        ('Insurance ',{'fields':['insurance_company','insurance_Number']}),
     )

class TestAdmin(ImportExportModelAdmin):
    resource_class = TestResource
    fieldsets = (
        ('Test Info', {'fields': ['id','name']}),
        ('Test Prices :', {'fields': ['max_1995','min_1995','min_price','max_2008','jam']})
    )

admin.site.register(Reports)

admin.site.register(Doctor,DoctorAdmin)
admin.site.register(Insurance)
# admin.site.register(city,LeafletGeoAdmin)
admin.site.register(Area,LeafletGeoAdmin)
admin.site.register(Lab,LabAdmin)
admin.site.register(Test,TestAdmin)
admin.site.register(Patient,PatientAdmin)



