from django.shortcuts import render
from django.views.decorators.clickjacking import xframe_options_exempt
from django.views.decorators.clickjacking import xframe_options_sameorigin
from .models import *

# Create your views here.
@xframe_options_exempt
def guide(request):

    context = {
        'news': News.objects.all().first()
    }
    return render(request, 'guide.html', context)

def home(request):
    return render(request, 'home.html')

@xframe_options_sameorigin
def panaroma(request):
    return render(request, 'panaroma.html')