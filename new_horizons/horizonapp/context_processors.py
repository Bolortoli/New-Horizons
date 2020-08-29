from .models import Settings, FloorPlan

def global_settings(request):

    if not FloorPlan.objects.exists():
        FloorPlan(floor='B1').save()
        for i in range(1, 16):
            FloorPlan(floor=i).save()

    return {
        'global_settings': Settings.objects.all()[0] if Settings.objects.count() != 0 else Settings.objects.all(),
    }