from django.shortcuts import render
from mysite.customers.models import Customers


def customers(request):
    objects = Customers.objects.all()
    return render(request, 'customers.html', context={'customers': objects})


def customers_plus(request):
    # print('customers')
    # import pdb; pdb.set_trace()
    # return customers(request)
    # pass
    my_objects = Customers.objects.filter(default=True)
    return render(request, 'customers/plus.html', context={'customers': my_objects })

