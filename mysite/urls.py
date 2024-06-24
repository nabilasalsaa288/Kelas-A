"""
URL configuration for mysite project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
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
from django.urls import path,include

from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf.urls.static import static
from django.conf import settings
from mysite.views import home,detail_artikel,about,contact
from mysite.authentikasi import akun_login,akun_registarasi,akun_logout

from berita.api  import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('about/', about, name='about'),
    path('artikel/<slug:slug>', detail_artikel, name='detail_artikel'),
    path('contact/', contact, name='contact'),
    path('dashboard/', include('berita.urls')),

    path('authentikasi/login', akun_login, name='akun_login'),
    path('authentikasi/registarasi', akun_registarasi, name='akun_registarasi'),
    path('authentikasi/logout', akun_logout, name='akun_logout'),

    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('api-auth/', include('rest_framework.urls')),


    path('api/kategori/list', api_kategori_list, name='api-kategori-list'),
    path('api/kategori/detail/<int:id_kategori>', api_kategori_detail, name='api-kategori-detail'),
    path('api/kategori/add', api_kategori_add, name='api-kategori-add'),

    path('api/artikel/list', api_artikel_list, name='api-artikel-list'),
    path('api/artikel/detail/<int:id_artikel>', api_artikel_detail, name='api-artikel-detail'),
    path('api/artikel/add', api_artikel_add, name='api-artikel-add'),


    path('api/author/list', api_penulis_list, name='api-penulis-list'),
]

urlpatterns += staticfiles_urlpatterns()
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
