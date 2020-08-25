from django.contrib import admin
from .models import *
from django.forms import Textarea, TextInput
from django.contrib.auth.models import Group, User


admin.site.unregister(Group)
admin.site.unregister(User)
admin.site.site_header = 'New Hozirons Dashboard'

admin.site.register(News)
# admin.site.register(BuildingRents)
admin.site.register(NewsCategory)
admin.site.register(OrganizationCategory)
admin.site.register(HomeSlider)
admin.site.register(RentedFloor)
admin.site.register(ContactUs)
@admin.register(BuildingRents)
class BuildingRentsAdmin(admin.ModelAdmin):

    def changelist_view(self, request, extra_context=None):
        extra_context = extra_context or {}
        extra_context['some_var'] = 'This is what I want to show'
        return super(BuildingRentsAdmin, self).changelist_view(request, extra_context=extra_context)


# @admin.register(NewsCategory)
# class NewsAdmin(admin.ModelAdmin):
#     inlines = [ReasonBoxesInline]
class OrganizationInline(admin.TabularInline):
    model = OrganizationDetail
        
@admin.register(Organization)
class OrganizationAdmin(admin.ModelAdmin):
    inlines = [OrganizationInline]

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

@admin.register(PDFbrochure)
class PDFbrochureAdmin(admin.ModelAdmin):
    list_display = [f.name for f in PDFbrochure._meta.get_fields()]
    list_editable = [f.name for f in PDFbrochure._meta.get_fields() if f.name != "id" and f.name != "title"]

    formfield_overrides = {
        models.TextField: {'widget': Textarea(attrs={'rows':4, 'cols':130})},
    }

    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False


@admin.register(FeatureCard)
class FeatureCardAdmin(admin.ModelAdmin):

    list_display = [f.name for f in FeatureCard._meta.get_fields()]
    list_editable = [f.name for f in FeatureCard._meta.get_fields() if f.name != "id" and f.name != "title"]

    formfield_overrides = {
        models.TextField: {'widget': Textarea(attrs={'rows':4, 'cols':30})},
    }

    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False