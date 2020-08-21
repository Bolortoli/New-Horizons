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

    reason_boxes = ReasonBoxes.objects.all().first() if ReasonBoxes.objects.count() != 0 else ReasonBoxes.objects.all()
    pdf_url = PDFbrochure.objects.all().first().pdf
    feature_boxes = FeatureCard.objects.all().first() if FeatureCard.objects.count() != 0 else FeatureCard.objects.all()
    home_sliders = HomeSlider.objects.all()

    context = {
        'reason_boxes': reason_boxes,
        'pdf_url': pdf_url,
        'feature_boxes': feature_boxes,
        'home_sliders': home_sliders
    }

    return render(request, 'home.html', context)

@xframe_options_sameorigin
def panaroma(request):
    return render(request, 'panaroma.html')

def news_blog_archive(request):
    return render(request, 'blog.single.html')

def blog(request):
    return render(request, 'blog.html')

@csrf_exempt
def get_building_rent_details(request):
    # TODO remove hard CODE!!!
    # json = {}
    # for field in BuildingRents._meta.get_fields():
    #     if field.name != "id":
    #         data = {str(field.name), str(BuildingRents.objects.all().first().(field.name))}

    # return JsonResponse({str(nameof(BuildingRents.objects.all().first().floor1_a)): "hell"})
    return JsonResponse({"floor1_a": str(BuildingRents.objects.all().first().floor1_a),
        "floor1_b": str(BuildingRents.objects.all().first().floor1_b),
        "floor2_a": str(BuildingRents.objects.all().first().floor2_a),
        "floor2_b": str(BuildingRents.objects.all().first().floor2_b),
        "floor3_a": str(BuildingRents.objects.all().first().floor3_a),
        "floor3_b": str(BuildingRents.objects.all().first().floor3_b),
        "floor4_a": str(BuildingRents.objects.all().first().floor4_a),
        "floor4_b": str(BuildingRents.objects.all().first().floor4_b),
        "floor5_a": str(BuildingRents.objects.all().first().floor5_a),
        "floor5_b": str(BuildingRents.objects.all().first().floor5_b),
        "floor6_a": str(BuildingRents.objects.all().first().floor6_a),
        "floor6_b": str(BuildingRents.objects.all().first().floor6_b),
        "floor7_a": str(BuildingRents.objects.all().first().floor7_a),
        "floor7_b": str(BuildingRents.objects.all().first().floor7_b),
        "floor8_a": str(BuildingRents.objects.all().first().floor8_a),
        "floor8_b": str(BuildingRents.objects.all().first().floor8_b),
        "floor9_a": str(BuildingRents.objects.all().first().floor9_a),
        "floor9_b": str(BuildingRents.objects.all().first().floor9_b),
        "floor10_a": str(BuildingRents.objects.all().first().floor10_a),
        "floor10_b": str(BuildingRents.objects.all().first().floor10_b),
        "floor11_a": str(BuildingRents.objects.all().first().floor11_a),
        "floor11_b": str(BuildingRents.objects.all().first().floor11_b),
        "floor12_a": str(BuildingRents.objects.all().first().floor12_a),
        "floor12_b": str(BuildingRents.objects.all().first().floor12_b),
        "floor13_a": str(BuildingRents.objects.all().first().floor13_a),
        "floor13_b": str(BuildingRents.objects.all().first().floor13_b),
        "floor14_a": str(BuildingRents.objects.all().first().floor14_a),
        "floor14_b": str(BuildingRents.objects.all().first().floor14_b),
        "floor15_a": str(BuildingRents.objects.all().first().floor15_a),
        "floor15_b": str(BuildingRents.objects.all().first().floor15_b),
    })

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
