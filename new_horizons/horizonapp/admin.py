from django.contrib import admin
from .models import *
from django.forms import Textarea, TextInput
from django.contrib.auth.models import Group, User


admin.site.unregister(Group)
admin.site.unregister(User)
admin.site.site_header = 'New Hozirons Dashboard'

admin.site.register(NewsCategory)
admin.site.register(News)
admin.site.register(BuildingRents)

# @admin.register(BuildingRents)
# class BuildingRentsAdmin(admin.ModelAdmin):

#     def response_change(self, request, obj):
#         if "_continue" in request.POST:

@admin.register(ReasonBoxes)
class ReasonBoxesAdmin(admin.ModelAdmin):
    list_display = [f.name for f in ReasonBoxes._meta.get_fields()]
    list_editable = [f.name for f in ReasonBoxes._meta.get_fields() if f.name != "id" and f.name != "title"]
    
    formfield_overrides = {
        models.CharField: {'widget': TextInput(attrs={'size':'20'})},
        models.TextField: {'widget': Textarea(attrs={'rows':4, 'cols':40})},
    }
    
@admin.register(Settings)
class SettingsAdmin(admin.ModelAdmin):
    list_display = [f.name for f in Settings._meta.get_fields()]
    list_editable = [f.name for f in Settings._meta.get_fields() if f.name != "id" and f.name != "title"]
    
    formfield_overrides = {
        models.CharField: {'widget': TextInput(attrs={'size':'20'})},
        models.TextField: {'widget': Textarea(attrs={'rows':4, 'cols':40})},
    }
    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

admin.site.register(PDFbrochure)