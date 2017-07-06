"""wedding_planner URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.auth import views as auth_views

from planner.views import *


urlpatterns = [
    url(r'^admin/', admin.site.urls, name="admin"),

    url(r'^base/$', BaseView.as_view()),
    url(r'^menu/$', MenuView.as_view()),
    url(r'^create/wedding-hall/', WeddingHallCreateView.as_view()),
    url(r'^create/car/', CarCreateView.as_view()),
    url(r'^create/photographer/', PhotographerCreateView.as_view()),
    url(r'^create/band/', BandCreateView.as_view()),
    url(r'^create/wedding-rings/', WeddingRingsCreateView.as_view()),
    url(r'^create/alcohol-beverages/', AlcoholBeveragesCreateView.as_view()),
    url(r'^create/non-alcohol-beverages/', NonAlcoholBeveragesCreateView.as_view()),
    url(r'^create/church/', ChurchCreateView.as_view()),
    url(r'^create/other/', OtherCreateView.as_view()),



    url(r'^signup/$', signup, name='signup'),
    url(r'^$', auth_views.login, name='login'),
    url(r'^logout/$', auth_views.logout, {'next_page': '/'}, name='logout'),



] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
