from .models import *

def global_settings(request):

    if not Three60Pic.objects.exists():
        Three60Pic().save()

    if not BuildingEnvironment.objects.exists():
        BuildingEnvironment().save()

    if not BuildingRents.objects.exists():
        BuildingRents().save()

    if not FloorPlan.objects.exists():
        FloorPlan(floor='B1').save()
        for i in range(1, 16):
            FloorPlan(floor=i).save()

    if not ReasonBoxes.objects.exists():
        ReasonBoxes(language='Монгол').save()
        ReasonBoxes(language='English').save()

    if not HomeSlider.objects.exists():
        HomeSlider().save()
    
    if not FeatureCard.objects.exists():
        FeatureCard(language='Монгол').save()
        FeatureCard(language='English').save()

    if not BuildingIntro.objects.exists():
        BuildingIntro().save()

    if not SubPage.objects.exists():
        SubPage(page_title='Бидний тухай', sign='1').save()
        SubPage(page_title='Аюулгүй байдал', sign='2').save()
        SubPage(page_title='Барилгын төлөвлөлт', sign='3').save()
        SubPage(page_title='Тав тух', sign='4').save()
    
    if not PDFbrochure.objects.exists():
        PDFbrochure().save()

    if not Settings.objects.exists():
        Settings().save()

    # if not GuidePic.objects.exists():
    #     GuidePic().save()

    subpages = []

    for page in SubPage.objects.all():
        subpages.append({
            'title': page.page_title,
            'sign': page.sign
        })

    if not NewsCategory.objects.exists():
      shineTalbai = NewsCategory(name="Шинэ Талбай",name_eng="Available Floor")
      shineTalbai.save()
      ulsTur = NewsCategory(name="Улс Төр",name_eng="Government")
      ulsTur.save()
      niigem = NewsCategory(name="Нийгэм",name_eng="Economy")
      niigem.save()


    return {
        'global_settings': Settings.objects.all().first(),
        'subpages': subpages,
    }
