from django.shortcuts import render
from django.shortcuts import redirect
from mysite.customers.models import Customers


def customers(request):
    objects = Customers.objects.all()
    return render(request, 'customers.html', context={'customers': objects})


def customers_plus(request):
    pass

