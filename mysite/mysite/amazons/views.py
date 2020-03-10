from django.shortcuts import render
from django.shortcuts import redirect
from mysite.amazons.models import Amazons


def amazons(request):
    ama = Amazons.objects.all()
    return render(request, 'amazons.html', context={'amazons': ama})

def amazons_plus(request):
    amazon_id = int(request.POST.get("amazon_id"))
    amazon = Amazons.objects.get(pk=amazon_id)
    months = [amazon.month_1, amazon.month_2, amazon.month_3, amazon.month_4]
    for month in months:
        if month == True:
            amazon.save()
    return redirect('amazon-list')