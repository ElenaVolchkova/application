from django.shortcuts import render
from django.shortcuts import redirect
from mysite.amazons.models import Amazons
from mysite.ward.models import Ward


def amazons(request):
    ama = Amazons.objects.all()
    return render(request, 'amazons.html', context={'amazons': ama})

def amazons_plus(request):
    amazon_id = int(request.POST.get("amazon_id"))
    amazon = Amazons.objects.get(pk=amazon_id)
    # months = [amazon.month_1, amazon.month_2, amazon.month_3, amazon.month_4]
    month_id = int(request.POST.get("month_id"))
    months = Amazons.objects.get(pk=month_id)
    for month in months:
        if month == True:
            amazon.save()
    return redirect('amazon-list')

def amazons_new(request):
    name = request.POST.get("name")
    ward = Ward.objects.create(ward=name)
    ward.save()
    ama = Amazons.objects.create(ward_id=ward)
    ama.save()
    return redirect('amazon-list')
