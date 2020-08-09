from django.urls import path, include
from . import views
from django.views.generic import TemplateView

urlpatterns = [
    path('', views.index, name="index"),
    path('panaroma/', TemplateView.as_view(template_name='panaroma.html'), name='panaroma')
]