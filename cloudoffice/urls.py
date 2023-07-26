"""cloudoffice URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.INDEX, name = 'index'),
    path('Plant_trial/',views.Plant_trial, name = 'Plant_trial'),
    path('Plant_trial_view/', views.Plant_trial_view, name='Plant_trial_view'),
    path('Plant_trial_view', views.Trial_data_download, name='Trial_data_download'),
    path('market_sample/',views.market_sample, name = 'market_sample'),
    path('market_sample_view/',views.market_sample_view, name = 'market_sample_view'),
    path('market_sample_view', views.market_sample_download, name='market_sample_download'),
    path('market_image_upload/', views.market_image_upload , name='market_image_upload'),
    path('market_image_view/', views.market_image_view, name='market_image_view'),
    path('market_complaint/',views.market_complaint, name = 'market_complaint'),
    path('market_complaint_view/',views.market_complaint_view, name = 'market_complaint_view'),
    path('market_complaint_view', views.market_complaint_download, name='market_complaint_download'),
    path('test_sample/',views.test_sample, name = 'test_sample'),
    path('test_sample_view/',views.test_sample_view, name = 'test_sample_view'),
    path('testsample_image_upload/', views.testsample_image_upload , name='testsample_image_upload'),
    path('testsample_image_view/', views.testsample_image_view, name='testsample_image_view'),
    path('accounts/', views.accounts_data, name='accounts'),
    path('accounts_view/',views.accounts_view, name = 'accounts_view'),


]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG:
        urlpatterns += static(settings.MEDIA_URL,
                              document_root=settings.MEDIA_ROOT)
