from django.contrib import admin
from .models import *
from django.forms import Textarea, TextInput
from django.contrib.auth.models import Group, User


admin.site.unregister(Group)
admin.site.unregister(User)
admin.site.site_header = 'New Hozirons Dashboard'

admin.site.register(NewsCategory)
admin.site.register(OrganizationCategory)
admin.site.register(HomeSlider)
# admin.site.register(RentedFloor)
@admin.register(ContactUs)
class ContactUsAdmin(admin.ModelAdmin):

    list_display = [f.name for f in ContactUs._meta.get_fields() if f.name != 'id']
    list_display_links = None

    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return True

@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'featured']
    list_editable = ['featured']

@admin.register(BuildingIntro)
class BuildingIntroAdmin(admin.ModelAdmin):

    list_display = [f.name for f in BuildingIntro._meta.get_fields()]
    list_editable = [f.name for f in BuildingIntro._meta.get_fields() if f.name != "id" and f.name != "title"]
    list_display_links = None

    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False

@admin.register(BuildingRents)
class BuildingRentsAdmin(admin.ModelAdmin):

    def changelist_view(self, request, extra_context=None):
        extra_context = extra_context or {}
        extra_context['some_var'] = 'This is what I want to show'
        return super(BuildingRentsAdmin, self).changelist_view(request, extra_context=extra_context)

    def has_add_permission(self, request):
            return False

    def has_delete_permission(self, request, obj=None):
        return False

class OrganizationInline(admin.TabularInline):
    model = OrganizationDetail
        
@admin.register(Organization)
class OrganizationAdmin(admin.ModelAdmin):
    inlines = [OrganizationInline]

    list_display = ['or_name', 'category', 'pic', 'special']
    list_editable = ['category', 'pic', 'special']

@admin.register(ReasonBoxes)
class ReasonBoxesAdmin(admin.ModelAdmin):
    list_display = [f.name for f in ReasonBoxes._meta.get_fields()]
    list_editable = [f.name for f in ReasonBoxes._meta.get_fields() if f.name != "id" and f.name != "title"]
    list_display_links = None

    formfield_overrides = {
        models.CharField: {'widget': TextInput(attrs={'size':'20'})},
        models.TextField: {'widget': Textarea(attrs={'rows':4, 'cols':40})},
    }

    def has_add_permission(self, request):
            return False

    def has_delete_permission(self, request, obj=None):
        return False

    
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
    list_display = ['pdf']
    list_editable = ['pdf']
    list_display_links = None
    formfield_overrides = {
        models.TextField: {'widget': Textarea(attrs={'rows':1, 'cols':130})},
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

@admin.register(FloorPlan)
class FloorPlanAdmin(admin.ModelAdmin):
    
    list_display = ['floor', 'pic']
    list_editable = ['pic']
    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False


class SubPage_NoTitledIconLeftInline(admin.TabularInline):
    model = SubPages_NoTitleIcon_Leftpic

class SubPage_NoTitledIconRightInline(admin.TabularInline):
    model = SubPages_NoTitleIcon_Rightpic

class SubPage_TitledIconInline(admin.TabularInline):
    model = SubPages_TitleIcon

class SubPage_SliderInline(admin.TabularInline):
    model = SubPages_Slider

@admin.register(SubPage)
class SubPageAdmin(admin.ModelAdmin):
    inlines = [SubPage_NoTitledIconLeftInline, SubPage_NoTitledIconRightInline, SubPage_TitledIconInline, SubPage_SliderInline]

    def has_add_permission(self, request):
        return False

    def has_delete_permission(self, request, obj=None):
        return False
