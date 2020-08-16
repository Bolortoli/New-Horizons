from django.shortcuts import render
from django.views.decorators.clickjacking import xframe_options_exempt
from django.views.decorators.clickjacking import xframe_options_sameorigin
from .models import *

# Create your views here.
@xframe_options_exempt
def guide(request):

<<<<<<< HEAD
    # context = {
    #     'news': News.objects.all().first()
    # }
    return render(request, 'guide.html')
=======
    context = {
        'news': News.objects.all().first()
    }
    return render(request, 'blog.single.html', context)
>>>>>>> f72e882e0d5936885945d675abba47138aa3f07f

def home(request):
    return render(request, 'home.html')

@xframe_options_sameorigin
def panaroma(request):
    return render(request, 'panaroma.html')