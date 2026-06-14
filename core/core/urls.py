"""
URL configuration for core project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.0/topics/http/urls/
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
from home.views import home
from home.views import successpage
from home.views import *
from vege.views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [

    # when used comes in '' means main page it calls home functioin inside the home views
    path('',home,name="home"),
    path('succ-page/',successpage,name="success"),
    path('delete-rec/<id>/' ,delete_receipe, name="delete_receipe" ),
    path('update-rec/<id>/' ,update_receipe, name="update_receipe" ),
    path('rec/',rec_show,name="recepy"),
    path('contact/',contact,name="contact"),
    path('about/',about,name="about"),
    path('admin/', admin.site.urls),
    
]
if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT
    )
