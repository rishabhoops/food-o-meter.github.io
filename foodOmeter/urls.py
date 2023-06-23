"""
URL configuration for foodOmeter project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from foodOmeterApp import views
from django.conf import settings
from django.conf.urls.static import static
from django.views.static import serve
from django.urls import re_path as url


urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index),
    path('aboutus/',views.aboutusPage),
    path('contactus/',views.contactusPage),
    path('services/',views.servicePage),
    path('menu/',views.menuPage),
    path('login/',views.loginPage),
    path('register/',views.register),
    path('check_user_exist/',views.check_user_exist, name="check_user_exist"),
    path('dashboard/',views.Dashboard),
    path('logout/',views.user_logout,name='logout'),
    path('forget_password/',views.forget_password),
    path('change_password/<token>/',views.change_password),
    path('cart/',views.cart),
    path('checkout/',views.checkout),
    path('order-sucess/',views.order_sucess),
    url(r'^media/(?P<path>.*)$', serve,{'document_root':       settings.MEDIA_ROOT}), 
    url(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}),
    
]

if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)