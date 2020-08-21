from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from django.views.decorators.clickjacking import xframe_options_exempt, xframe_options_sameorigin
from .models import *
from django.http import HttpResponse, JsonResponse
from django.core.mail import EmailMessage


def guide(request):

    return render(request, 'guide.html')

@xframe_options_exempt
def home(request):

    reason_boxes = ReasonBoxes.objects.all()[0] if ReasonBoxes.objects.count() != 0 else ReasonBoxes.objects.all()
    pdf_url = PDFbrochure.objects.all().first().pdf

    context = {
        'reason_boxes': reason_boxes,
        'pdf_url': pdf_url,
    }

    return render(request, 'home.html', context)

@xframe_options_sameorigin
def panaroma(request):
    return render(request, 'panaroma.html')

<<<<<<< HEAD
def blog(request):
    return render(request, 'blog.html')
=======
def news_blog_archive(request):
    return render(request, 'blog.html')


# @csrf_exempt
# def send_email(request):
#     s = PDFbrochure.objects.all()

#     if not s:
#         print('kk')
#         return JsonResponse({"message": "Уучлаарай. Одоогоор брошур байхгүй байна."})
#     else: 
#         # email_subject = PDF.objects.all()

#         email=EmailMessage(
#             'New horizon'.encode('utf-8'),
#             'body'.encode('utf-8'),
#             'bolortoli@csms.edu.mn',
#             to=['boogiibobko@gmail.com'],
#         )
#         email.content_subtype = 'html'
        
#         with open(PDFbrochure.objects.all().first().pdf.path, mode='rb') as file:
#             q = file.read().decode('utf-8')
#             email.attach(file.name, q)
#             email.send()
#             print('asd')
        
#         return HttpResponse("yes")
>>>>>>> f4bcf7081e4b4bd00cea1fd474b5c02d5a469c6c
