"""alcohol URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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

from xml.etree.ElementInclude import include
from django.contrib import admin
from django.urls import path
from alcohol import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.homepage),                     #home page direct call hoga 127.0.0.1907
    path('about/', views.about),
    path('about/<int:python>', views.python),                    #dynamic urls creation ways pyhton ek function hh view.py m
    path('career/', views.career),
    path('career/<str:python>', views.python),                  #dynamic urls creation ways pyhton ek function hh view.py m
    path('service/', views.service),
    path('register/', views.designregister),
    path('userformget/', views.userformget),
    
    path('userformpostredirect/', views.userformpostredirect),

    path('userformpostaction/', views.userformpostaction),
    path('submitform/', views.submitform,name="submitform"),                       #action part for submit

    path('djangoform/', views.djangoform),
    path('submitform1/', views.submitform1,name="submitform1"),
    
    path('formfordatabase/', views.formfordatabase),
    path('saveenquiry/', views.saveenquiry,name="saveenquiry"),
    path('calculator/', views.calculator),
    path('newsdetails/<newsid>', views.newsdetails),
]

