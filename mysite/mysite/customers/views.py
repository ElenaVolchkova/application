from django.shortcuts import render
from django.shortcuts import redirect
from mysite.customers.models import Customers
from mysite.ward.models import Ward


def customers(request):
    objects = Customers.objects.all()
    return render(request, 'customers.html', context={'customers': objects})

def customers_plus(request):
    customer_id = int(request.POST.get("customer_id"))
    customer = Customers.objects.get(pk=customer_id)
    day_id = int(request.POST.get("day_id"))
    days = Customers.objects.get(pk=day_id)
    for day in days:
        if day == True:
            customer.save()
    return redirect('customer-list')

def customers_new(request):
    name = request.POST.get("name")
    if name not in [y.ward for y in Ward.objects.all()]:
        ward = Ward.objects.create(ward=name)
        ward.save()
        objects = Customers.objects.create(ward_id=ward)
        objects.save()
        return redirect('customer-list')
    else:
        return redirect('customer-list')