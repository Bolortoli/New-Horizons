from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from django.views.decorators.clickjacking import xframe_options_exempt, xframe_options_sameorigin
from .models import *
from django.http import HttpResponse, JsonResponse, HttpResponseBadRequest
from django.core.mail import EmailMessage
import json, random
from django.core.paginator import Paginator 
from django.utils.translation import gettext as _

FEATURE_NEWS_ON_BLOGS = 4
FEATURE_NEWS_ON_HOME = 3

def guide(request):

    try :
      pdf = PDFbrochure.objects.all().first()
    except:
      new_pdf_obj = PDFbrochure.objects.create(pdf="https://drive.google.com/file/d/1X7DCnk5kRnHOjiVvGe32TOWqAk2M2isu/view?ts=5f0287df")
      new_pdf_obj.save()
      pdf = PDFbrochure.objects.all().first()

    pages = []
    # pics = GuidePic.objects.all().first()

    for page in SubPage.objects.all():
        pages.append({
            'title': page.page_title,
            'sign': str(page.sign)
        }.copy())

        print(pages)
    context = {
        'pdf_url': pdf,
        'sub_pages': pages,
        # 'pics': pics,
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
    reason_boxes_eng = ReasonBoxes.objects.get(language='Монгол')
    reason_boxes_mon = ReasonBoxes.objects.get(language='English')
    pdf_url = PDFbrochure.objects.all().first()
    feature_boxes_mon = FeatureCard.objects.get(language='Монгол')
    feature_boxes_eng = FeatureCard.objects.get(language='English')
    home_sliders = HomeSlider.objects.all()
    building_intro = BuildingIntro.objects.all().first() if BuildingIntro.objects.count() != 0 else None

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
    # Custom url company -> means companies slider on home page
    else:
        leaseholder_slider = []
        sliders = OrganizationDetail.objects.filter(organization=Organization.objects.get(id=company))
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
                org_cats['leaseholder'].append(Organization.objects.get(or_name=org.or_name))
                # orgs.append()
            orgs.append(org_cats)

    # LEASEHOLDERS on building
    leaseholder_per_floor = []
    # if RentedFloor.objects.exists():
    for i in range(15, 0, -1):
        fa = RentedFloor.objects.filter(rented_object='id_floor'+str(i)+'_a')
        fb = RentedFloor.objects.filter(rented_object='id_floor'+str(i)+'_b') 
        # if floor_filter_a.exist():
        #     leaseholder_per_floor.append(floor_rent(floor_filter_a.first().organization.pic, name=str(i)+'-a'))
        
        # if floor_filter_b.exist():
        #     leaseholder_per_floor.append(floor_rent(floor_filter_b.first().organization.pic, name=str(i)+'-b'))
        if fa.exists() and fb.exists():
            leaseholder_per_floor.append(floor_rent(floor=i, picture1=fa.first().organization.pic, name1=fa.first().organization.or_name, picture2=fb.first().organization.pic, name2=fb.first().organization.or_name))
        elif fa.exists() and not fb.exists():
            leaseholder_per_floor.append(floor_rent(floor=i, picture1=fa.first().organization.pic, name1=fa.first().organization.or_name, picture2=None, name2=None))
        elif not fa.exists() and fb.exists():
            leaseholder_per_floor.append(floor_rent(floor=i, picture2=fb.first().organization.pic, name2=fb.first().organization.or_name, picture1=None, name1=None))
        else:
            leaseholder_per_floor.append(floor_rent(floor=i, picture1=None, name1=None, picture2=None, name2=None))
    leaseholder_per_floor.append(floor_rent(floor='B1', picture1=None, name1=None, picture2=None, name2=None, b1=True))

        # for rentedfloor in RentedFloor.objects.all():
        #     # floor = rentedfloor.
        #     leaseholder_per_floor.append(rentedfloor)

    # Floors plan images
    floor_plan_details = []
    for plan in FloorPlan.objects.all().exclude(floor="B1").order_by('-id'):
        # print(plan.title)
        floor_plan_details.append(plan)                 
    floor_plan_details.append(FloorPlan.objects.get(floor='B1'))
    print(floor_plan_details[15].pic)
    
    # Featured news
    news_list = []
    if News.objects.exists():
        for news in News.objects.filter(featured=True)[:FEATURE_NEWS_ON_HOME]:
            news_list.append(news)

    # Building environment slider
    env_obj = BuildingEnvironment.objects.all().first()
    env_pics = BuildingEnvironmentPic.objects.filter(organization=env_obj)
    
    # 360 pictures
    three60pic = Three60Pic.objects.all().first()

    context = {
        'reason_boxes_eng': reason_boxes_eng,
        'reason_boxes_mon': reason_boxes_mon,
        'pdf_url': pdf_url,
        'feature_boxes_eng': feature_boxes_eng,
        'feature_boxes_mon': feature_boxes_mon,
        'home_sliders': home_sliders,
        'lesaeholder_slider': leaseholder_slider,
        'leaseholders': orgs,
        'intro': building_intro,
        'floor_plan': floor_plan_details,
        'leaseholder_per_floor': leaseholder_per_floor,
        'news_list': news_list,
        'env_obj': env_obj,
        'env_pics': env_pics,
        'three60pic': three60pic,
    }

    return render(request, 'home.html', context)

@xframe_options_sameorigin
def panaroma(request):
    three60pic = Three60Pic.objects.all().first()

    context = {
        'three60pic': three60pic,
    }
    return render(request, 'panaroma.html', context)

def news_blog_archive(request):

    obj_list = News.objects.all()

    paginator = Paginator(obj_list, 6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    featured_news = News.objects.filter(featured=True)[:FEATURE_NEWS_ON_BLOGS]

    categories = [News_Category(cat, News.objects.filter(category=cat).count(), NewsCategory.objects.get(name=cat.name).id) for cat in NewsCategory.objects.all() if News.objects.filter(category=cat).count() != 0]

    pdf = PDFbrochure.objects.all().first().pdf

    context = {
        'news_list': page_obj,
        'featured_news': featured_news,
        'categories': categories,
        'pdf_url': pdf,
    }
    return render(request, 'blog.html', context)

def news_blog_archive_category(request, cat_id):

    obj_list = News.objects.filter(category=NewsCategory.objects.get(id=cat_id))

    paginator = Paginator(obj_list, 6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    featured_news = News.objects.filter(featured=True)[:FEATURE_NEWS_ON_BLOGS]

    categories = [News_Category(cat, News.objects.filter(category=cat).count(), NewsCategory.objects.get(name=cat.name).id) for cat in NewsCategory.objects.all() if News.objects.filter(category=cat).count() != 0]

    pdf = PDFbrochure.objects.all().first().pdf

    context = {
        'news_list': page_obj,
        'featured_news': featured_news,
        'categories': categories,
        'pdf_url': pdf,
    }
    return render(request, 'blog.html', context)

def subpage(request, sign):
    page_obj = SubPage.objects.get(sign=sign)
    notitlediconleft = SubPages_NoTitleIcon_Leftpic.objects.filter(organization=page_obj)
    print(notitlediconleft)
    if not notitlediconleft:
        print('agaign') 
    notitlediconright = SubPages_NoTitleIcon_Rightpic.objects.filter(organization=page_obj)
    titledicon = SubPages_TitleIcon.objects.filter(organization=page_obj)
    slider = SubPages_Slider.objects.filter(organization=page_obj)
    # security = SubPage.objects.get(sign='2').page_title
    # building_structure = SubPage.objects.get(sign='3').page_title
    # user_experience = SubPage.objects.get(sign='4').page_title
    pages = []

    for page in SubPage.objects.all().exclude(sign=sign):
        pages.append({
            'title': page.page_title,
            'title_eng': page.page_title_eng,
            'sign': page.sign
        })

    context = {
        'page_obj': page_obj,
        'notitlediconleft': notitlediconleft,
        'notitlediconright': notitlediconright,
        'titledicon': titledicon,
        'slider': slider,
        'pages': pages
    }
    return render(request, 'subpage.html', context)

# def building_structure(request):
#     page_obj = SubPage.objects.get(sign='3')
#     notitlediconleft = SubPages_NoTitleIcon_Leftpic.objects.filter(organization=page_obj)
#     notitlediconright = SubPages_NoTitleIcon_Rightpic.objects.filter(organization=page_obj)
#     titledicon = SubPages_TitleIcon.objects.filter(organization=page_obj)
#     slider = SubPages_Slider.objects.filter(organization=page_obj)
#     security = SubPage.objects.get(sign='2').page_title
#     about_us = SubPage.objects.get(sign='1').page_title
#     user_experience = SubPage.objects.get(sign='4').page_title

#     context = {
#         'page_obj': page_obj,
#         'notitlediconleft': notitlediconleft,
#         'notitlediconright': notitlediconright,
#         'titledicon': titledicon,
#         'slider': slider,
#         'security': security,
#         'about_us': about_us,
#         'user_experience': user_experience,
#     }
#     return render(request, 'building_structure.html', context)
# def user_experience(request):

#     page_obj = SubPage.objects.get(sign='4')
#     notitlediconleft = SubPages_NoTitleIcon_Leftpic.objects.filter(organization=page_obj)
#     notitlediconright = SubPages_NoTitleIcon_Rightpic.objects.filter(organization=page_obj)
#     titledicon = SubPages_TitleIcon.objects.filter(organization=page_obj)
#     slider = SubPages_Slider.objects.filter(organization=page_obj)
#     security = SubPage.objects.get(sign='2').page_title
#     about_us = SubPage.objects.get(sign='1').page_title
#     building_structure = SubPage.objects.get(sign='3').page_title

#     context = {
#         'page_obj': page_obj,
#         'notitlediconleft': notitlediconleft,
#         'notitlediconright': notitlediconright,
#         'titledicon': titledicon,
#         'slider': slider,
#         'security': security,
#         'about_us': about_us,
#         'building_structure': building_structure,
#     }

#     return render(request, 'user_experience.html', context)
# def security(request):

#     page_obj = SubPage.objects.get(sign='2')
#     notitlediconleft = SubPages_NoTitleIcon_Leftpic.objects.filter(organization=page_obj)
#     notitlediconright = SubPages_NoTitleIcon_Rightpic.objects.filter(organization=page_obj)
#     titledicon = SubPages_TitleIcon.objects.filter(organization=page_obj)
#     slider = SubPages_Slider.objects.filter(organization=page_obj)
#     user_experience = SubPage.objects.get(sign='4').page_title
#     about_us = SubPage.objects.get(sign='1').page_title
#     building_structure = SubPage.objects.get(sign='3').page_title

#     context = {
#         'page_obj': page_obj,
#         'notitlediconleft': notitlediconleft,
#         'notitlediconright': notitlediconright,
#         'titledicon': titledicon,
#         'slider': slider,
#         'user_experience': user_experience,
#         'about_us': about_us,
#         'building_structure': building_structure,
#     }

#     return render(request, 'security.html', context)

def blog(request, slug=None):
    if slug is not None:
        news_filter = News.objects.filter(slug=slug)
        news = News.objects.get(slug=slug)

        # Increment viewed count
        views_count = news.viewed + 1
        news_filter.update(viewed=views_count)

        categories = [News_Category(cat, News.objects.filter(category=cat).count()) for cat in NewsCategory.objects.all() if News.objects.filter(category=cat).count() != 0]
        category_blog = news.category

        featured_news = News.objects.filter(featured=True)[:FEATURE_NEWS_ON_BLOGS]

        pdf_url = PDFbrochure.objects.all().first().pdf

        # Reward.objects.all().order_by('-year', '-month').exclude(slug=specified_slug)[:count] if Reward.objects.count() >= count else Reward.objects.all()  
        news_related = News.objects.order_by('?').exclude(slug=slug)[:FEATURE_NEWS_ON_HOME]

    context = {
        'news': news,
        'categories': categories,
        'category_blog': category_blog,
        'pdf_url': pdf_url,
        'featured_news': featured_news,
        'news_related': news_related,
    }
    return render(request, 'blog_single.html', context)


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
        data = {}
        data['rented_floors'] = []
        print(data)
        for obj in RentedFloor.objects.all():
            data['rented_floors'].append({
                'floor': obj.rented_object,
                'organization': obj.organization.or_name
            })

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

class floor_rent:
    def __init__(self, picture1, name1, picture2, name2, floor, b1=False):
        self.picture1 = picture1
        self.name1 = name1
        self.picture2 = picture2
        self.name2 = name2
        self.floor = floor
        self.b1 = b1

class News_Category:
    def __init__(self, category, news_count, cat_id=None):
        self.category = category
        self.news_count = news_count
        self.cat_id = cat_id
