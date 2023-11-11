"""
URL configuration for project5 project.

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
from app1.views import *
from app2.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('fun1ofapp1/',fun1ofapp1,name='fun1ofapp1'),
    path('fun2ofapp1/',fun2ofapp1,name='fun2ofapp1'),
    path('fun1ofapp2',fun1ofapp2,name='fun1ofapp2'),
    path('fun2ofapp2',fun2ofapp2,name='fun2ofapp2'),
]
