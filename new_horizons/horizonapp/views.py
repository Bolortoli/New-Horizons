from django.shortcuts import render
from django.views.decorators.clickjacking import xframe_options_exempt
from django.views.decorators.clickjacking import xframe_options_sameorigin
# Create your views here.
@xframe_options_exempt
def index(request):
    return render(request, 'home.html')

@xframe_options_sameorigin
def panaroma(request):
    return render(request, 'panaroma.html')