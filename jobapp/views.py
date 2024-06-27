from django.shortcuts import render
from jobapp.models import*

# Create your views here.
def home_viewpage(request):
    return render(request, 'jobapp/index.html')

def hydjobs(request):
    job_list = HydJobs.objects.all()
    type = 'hydjobs'
    my_dict = {'Job_list': job_list,'type':type} 

    return render(request, 'jobapp/hydjobs.html',my_dict)
def punejobs(request):
    job_list = PuneJobs.objects.all()
    type = 'punjobs'
    my_dict = {'Job_list': job_list, 'type':type} 
    return render(request, 'jobapp/hydjobs.html',my_dict)
def bngjobs(request):
    job_list = BangJobs.objects.all()
    type = 'BNG'
    my_dict = {'Job_list': job_list} 
    return render(request, 'jobapp/hydjobs.html',my_dict)