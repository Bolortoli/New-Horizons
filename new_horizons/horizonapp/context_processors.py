from .models import FloorPlan, SubPage, PDFbrochure, Settings, ReasonBoxes, HomeSlider, FeatureCard, BuildingIntro, BuildingRents, BuildingEnvironment

def global_settings(request):

    if not BuildingEnvironment.objects.exists():
        BuildingEnvironment().save()

    if not BuildingRents.objects.exists():
        BuildingRents().save()

    if not FloorPlan.objects.exists():
        FloorPlan(floor='B1').save()
        for i in range(1, 16):
            FloorPlan(floor=i).save()

    if not ReasonBoxes.objects.exists():
        ReasonBoxes().save()

    if not HomeSlider.objects.exists():
        HomeSlider().save()
    
    if not FeatureCard.objects.exists():
        FeatureCard().save()

    if not BuildingIntro.objects.exists():
        BuildingIntro().save()

    if not SubPage.objects.exists():
        # SubPage(page_title='Бидний тухай').save()
        # SubPage(page_title='Аюулгүй байдал').save()
        # SubPage(page_title='Барилгын төлөвлөлт').save()
        # SubPage(page_title='Тав тух').save()
        SubPage(page_title='Бидний тухай', sign='1').save()
        SubPage(page_title='Аюулгүй байдал', sign='2').save()
        SubPage(page_title='Барилгын төлөвлөлт', sign='3').save()
        SubPage(page_title='Тав тух', sign='4').save()
    
    if not PDFbrochure.objects.exists():
        PDFbrochure().save()

    if not Settings.objects.exists():
        Settings().save()
    return {
        'global_settings': Settings.objects.all().first()
    }