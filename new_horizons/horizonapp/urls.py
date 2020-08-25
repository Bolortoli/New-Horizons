from django.urls import path, include
from . import views
from django.views.generic import TemplateView

urlpatterns = [
    path('', views.guide, name="guide"),
    path('home/', views.home, name="home"),
    path('home/<str:company>', views.home, name='home'),
    path('panaroma/', views.panaroma, name='panaroma'),
    path('blog/', views.blog, name='blog'),
    path('news/', views.news_blog_archive, name='news'),
    path('get_building_rent_info', views.get_building_rent_details, name="get_building_rent_details"),
    path('get-organizations', views.get_organizations, name='get-organizations'),
    path('register-rent', views.register_rent, name='register-rent'),
    path('clear-leaseholder', views.clear_leaseholder, name='clear-leaseholder'),
    path('register-contact-requet', views.register_contact_request, name='register-contact-request')
]
