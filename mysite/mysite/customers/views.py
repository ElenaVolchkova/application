from django.shortcuts import render
from mysite.customers.models import Customers


def customers(request):
    objects = Customers.objects.all()
    return render(request, 'customers.html', context={'customers': objects})
