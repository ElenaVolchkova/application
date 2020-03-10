from django.shortcuts import render
from django.shortcuts import redirect
from mysite.customers.models import Customers


def customers(request):
    objects = Customers.objects.all()
    return render(request, 'customers.html', context={'customers': objects})

def customers_plus(request):
    customer_id = int(request.POST.get("customer_id"))
    customer = Customers.objects.get(pk=customer_id)
    days = [customer.day_1, customer.day_2, customer.day_3, customer.day_4, customer.day_5, customer.day_6]
    for day in days:
        if day == True:
            customer.save()
    return redirect('customer-list')
