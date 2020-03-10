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
from mysite.customers.views import customers, customers_plus
from mysite.athletes.views import athletes, athletes_plus
from mysite.amazons.views import amazons, amazons_plus

urlpatterns = [
    path('admin/', admin.site.urls),
    path('titova', titova),
    path('athletes', athletes, name='athlete-list'),
    path('athletes/plus', athletes_plus),
    path('amazons', amazons, name='amazon-list'),
    path('amazons/plus', amazons_plus),
    path('customers', customers, name='customer-list'),
    path('customers/plus', customers_plus)
]
