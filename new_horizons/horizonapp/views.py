from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from django.views.decorators.clickjacking import xframe_options_exempt, xframe_options_sameorigin
from .models import *
from django.http import HttpResponse, JsonResponse, HttpResponseBadRequest
from django.core.mail import EmailMessage
import json, random


def guide(request):
    co = BuildingRents.objects.all().first().floor2_a
    ca = BuildingRents.objects.all().first().floor2_b
    context = {
        'c': co,
        'co': ca,
    }
    return render(request, 'guide.html', context)

def get_organizations_with_slider(request):
    orgs = Organization.objects.all() 
    if orgs.count() == 0:
        return None
    return_data = {}
    # return_data.append([])
    for org in orgs:
        pass

@csrf_exempt
def register_contact_request(request):
    if request.method == 'POST':
        try:
            name = request.POST['name']
            email = request.POST['email']
            company = request.POST['company']
            text = request.POST['text']

            ContactUs(fullname=name, email=email, company=company, message=text).save()
            return HttpResponse()
        except Exception as e:
            print(e)
            return HttpResponseBadRequest()


@xframe_options_exempt
def home(request, company=None):
    reason_boxes = ReasonBoxes.objects.all().first() if ReasonBoxes.objects.count() != 0 else ReasonBoxes.objects.all()
    pdf_url = PDFbrochure.objects.all().first().pdf
    feature_boxes = FeatureCard.objects.all().first() if FeatureCard.objects.count() != 0 else FeatureCard.objects.all()
    home_sliders = HomeSlider.objects.all()

    if company is None:
        # LEASEHOLDER SLIDER INITIALIZE -->
        leaseholder_homepage_default = Organization.objects.filter(special=True)
        leaseholder_slider = []

        if not leaseholder_homepage_default.exists():
            if not Organization.objects.all().exists():
                leaseholder_slider = None
            else:
                # If not any special leaseholder return random
                leaseholder_homepage_default = random.choice(Organization.objects.all())
                sliders = OrganizationDetail.objects.filter(organization=leaseholder_homepage_default)
                for slider in sliders:
                    dictionary = {
                        'title': slider.title,
                        'desc': slider.desc,
                        'pic': slider.pic
                    }
                    leaseholder_slider.append(dictionary.copy())
        else:
            leaseholder_homepage_default = leaseholder_homepage_default.first()

            sliders = OrganizationDetail.objects.filter(organization=leaseholder_homepage_default)
            for slider in sliders:
                dictionary = {
                    'title': slider.title,
                    'desc': slider.desc,
                    'pic': slider.pic
                }
                leaseholder_slider.append(dictionary.copy())
            #     leaseholder_slider.append(slider)
        # END -->
    # Custom url company means companies slider on home page
    else:
        leaseholder_slider = []
        sliders = OrganizationDetail.objects.filter(organization=Organization.objects.get(or_name=company))
        for slider in sliders:
            dictionary = {
                'title': slider.title,
                'desc': slider.desc,
                'pic': slider.pic
            }
            leaseholder_slider.append(dictionary.copy())

    # LEASEHOLDERS category and names
    orgs = []
    if OrganizationCategory.objects.exists():
        for obj in OrganizationCategory.objects.all():
            org_cats = {
                'category': obj.category_name,
                'leaseholder': []
            }
            for org in Organization.objects.filter(category=obj):
                org_cats['leaseholder'].append(org.or_name)
                # orgs.append()
            orgs.append(org_cats)

    context = {
        'reason_boxes': reason_boxes,
        'pdf_url': pdf_url,
        'feature_boxes': feature_boxes,
        'home_sliders': home_sliders,
        'lesaeholder_slider': leaseholder_slider,
        'leaseholders': orgs,
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
def get_organizations(request):
    if request.method == 'POST':
        orgs_count = Organization.objects.count()
        data = {"success": "false"}

        if orgs_count == 0:
            return JsonResponse(data)

        orgs = Organization.objects.all()
        data = {"success": "true"}  
        data['organizations'] = []
        print(data)
        for organization in orgs:
            data['organizations'].append({
                'name': str(organization.or_name)
            })
        return JsonResponse(data)

@csrf_exempt
def clear_leaseholder(request):
    if request.method == 'POST':
        try:
            obj = RentedFloor.objects.get(rented_object=request.POST['floor_name'])
            obj.delete()
            return HttpResponse()
        except Exception as e:
            print(e)
            return HttpResponseBadRequest()

@csrf_exempt
def register_rent(request):
    if request.method == 'POST':
        try:
            floor_name = request.POST['floor_name']
            leaseholder_name = request.POST['leaseholder_name']
            rented_floor = RentedFloor.objects.filter(rented_object=floor_name).exists()
            if not rented_floor:
                RentedFloor(organization=Organization.objects.get(or_name=leaseholder_name)
                    ,rented_object=floor_name).save()
            else:
                obj = RentedFloor.objects.filter(rented_object=floor_name).first()
                obj.organization = Organization.objects.get(or_name=leaseholder_name)
                obj.rented_object = floor_name
                obj.save()
            return HttpResponse()

        except Exception as e:
            # print(e)
            return HttpResponseBadRequest()


@csrf_exempt
def get_building_rent_details(request):
    if request.method == 'POST':
        # TODO remove hard CODE!!! use eval or exec function
        data = {}
        data['rented_floors'] = []
        print(data)
        for obj in RentedFloor.objects.all():
            data['rented_floors'].append({
                'floor': obj.rented_object,
                'organization': obj.organization.or_name
            })


        # json = {}
        # for field in BuildingRents._meta.get_fields():
        #     if field.name != "id":
        #         data = {str(field.name), str(BuildingRents.objects.all().first().(field.name))}

        # return JsonResponse({str(nameof(BuildingRents.objects.all().first().floor1_a)): "hell"})
        return JsonResponse(data)

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
