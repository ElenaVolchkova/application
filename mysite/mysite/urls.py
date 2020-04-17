"""mysite URL Configuration

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
from django.contrib import admin
from django.urls import path
from mysite.titova.views import titova
from mysite.customers.views import customers, customers_plus, customers_new, customers_edit, customers_del
from mysite.athletes.views import athletes, athletes_plus, athletes_new, athletes_edit, athletes_del #, athletes_update
from mysite.amazons.views import amazons, amazons_plus, amazons_new, amazons_edit, amazons_del

from django.conf import settings
# from django.urls import path, re_path, include, reverse_lazy
from django.conf.urls.static import static
# from django.views.generic.base import RedirectView
# from rest_framework.routers import DefaultRouter
# from rest_framework.authtoken import views


# import pdb; pdb.set_trace()
urlpatterns = [
    path('admin/', admin.site.urls),
    path('titova', titova),
    path('athletes', athletes, name='athlete-list'),
    path('athletes/plus', athletes_plus),
    path('amazons', amazons, name='amazon-list'),
    path('amazons/plus', amazons_plus),
    path('customers', customers, name='customer-list'),
    path('customers/plus', customers_plus),
    path('amazons/new', amazons_new, name="amazons-new"),
    path('customers/new', customers_new, name="customers-new"),
    path('athletes/new', athletes_new, name="athletes-new"),
    path('amazons/edit/<int:id>/', amazons_edit, name="amazons-edit"),
    path('customers/edit/<int:id>/', customers_edit, name="customers-edit"),
    path('athletes/edit/<int:id>/', athletes_edit),
    path('athletes/del/<int:id>/', athletes_del),
    # path('athletes', athletes_update, name="athlete-edit"),
    path('customers/del/<int:id>/', customers_del, name="customers-del"),
    path('amazons/del/<int:id>/', amazons_del),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) #+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)