from django.shortcuts import render
from django.views.decorators.clickjacking import xframe_options_exempt, xframe_options_sameorigin
from .models import *

# Create your views here.
@xframe_options_exempt
def guide(request):

    context = {
        'rents': BuildingRents.objects.all().first()
    }
    return render(request, 'home.html', context)

def home(request):
    return render(request, 'home.html')

@xframe_options_sameorigin
def panaroma(request):
    return render(request, 'panaroma.html')

def blog(request):
    return render(request, 'blog.html')