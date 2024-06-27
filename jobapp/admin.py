from django.contrib import admin
from jobapp.models import HydJobs
from jobapp.models import PuneJobs
from jobapp.models import BangJobs

# Register your models here.
class HydJobs_Admin(admin.ModelAdmin):
    list_display = ['company','date','title','eligibilty','address','email','phonenumber']
admin.site.register(HydJobs,HydJobs_Admin)    

class PuneJobs_Admin(admin.ModelAdmin):
    list_display = ['date','company','title','eligibilty','address','email','phonenumber']
admin.site.register(PuneJobs,PuneJobs_Admin)    

class BngJobs_Admin(admin.ModelAdmin):
    list_display = ['date','company','title','eligibilty','address','email','phonenumber']
admin.site.register(BangJobs,BngJobs_Admin)    
