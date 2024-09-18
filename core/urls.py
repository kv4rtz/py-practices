"""
URL configuration for core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.urls import path, include
from django.shortcuts import render
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    
    # start: Практическая 7 
    path('', lambda req: render(req, 'home.html')),
    # end
    
    path('practice1/', include('practice1.urls')),
    path('practice2/', include('practice2.urls')),
    path('practice6/', include('practice6.urls')),
    path('practice7/', include('practice7.urls')),
    path('practice8/', include('practice8.urls')),
    path('practice9/', include('practice9.urls')),
    path('practice10/', include('practice10.urls')),
    path('practice11/', include('practice11.urls')),
    path('practice12/', include('practice12.urls')),
    path('practice13/', include('practice13.urls')),
    path('practice14/', include('practice14.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)