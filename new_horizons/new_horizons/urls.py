"""new_horizons URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from jet.dashboard.dashboard_modules import google_analytics_views
# from jet.dashboard.dashboard_modules import yandex_metrika_views
from django.contrib import admin
from django.urls import path, re_path, include
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls.i18n import i18n_patterns


urlpatterns = [  
    path('rosetta/', include('rosetta.urls')),
    re_path(r'^jet/', include('jet.urls', 'jet')),
    re_path(r'^jet/dashboard/', include('jet.dashboard.urls', 'jet-dashboard')),
    path('admin/', admin.site.urls),
    path('', include('horizonapp.urls')),
    path('secret/', include('admin_honeypot.urls', namespace='admin_honeypot')),
    # path('grappelli/', include('grappelli.urls')),
    path("ckeditor5/", include('django_ckeditor_5.urls')),
]

urlpatterns += i18n_patterns(
    path('', include('horizonapp.urls')),
)
