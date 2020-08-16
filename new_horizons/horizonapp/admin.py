from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(NewsCategory)
admin.site.register(News)
admin.site.register(BuildingRents)

# @admin.register(BuildingRents)
# class BuildingRentsAdmin(admin.ModelAdmin):

#     def response_change(self, request, obj):
#         if "_continue" in request.POST:
