"""My_First_WEB URL Configuration

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

from My_First_WEB import settings
from amcarservice.views import *
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('amcarservice/', include('amcarservice.urls')),
    path('django_tutorial/', include('django_tutorial.urls')),

]

#if settings.DEBUG:
    #  urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_URL)

#   handler404 = pageNoteFound
