from django.urls import path, include
from . import views
from django.views.generic import TemplateView

urlpatterns = [
    path('', views.guide, name="guide"),
    path('home/', views.home, name="home"),
<<<<<<< HEAD
    path('panaroma/', views.panaroma, name='panaroma'),
    path('blog/', views.blog, name='blog')
=======
    path('news/', views.news_blog_archive, name='news'),
    path('panaroma/', views.panaroma, name='panaroma'),
>>>>>>> f4bcf7081e4b4bd00cea1fd474b5c02d5a469c6c
]
