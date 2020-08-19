from django.urls import path, include
from . import views
from django.views.generic import TemplateView

urlpatterns = [
    path('', views.guide, name="guide"),
    path('home/', views.home, name="home"),
    path('news/', views.news_blog_archive, name='news'),
    path('panaroma/', views.panaroma, name='panaroma'),
]
