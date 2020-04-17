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
    month_id = int(request.POST.get("month_id"))
    months = Amazons.objects.get(pk=month_id)
    for month in months:
        if month == True:
            amazon.save()
    return redirect('amazon-list')

def amazons_new(request):
    name = request.POST.get("name")
    if name not in [y.ward for y in Ward.objects.all()]:
        ward = Ward.objects.create(ward=name)
        ward.save()
        ama = Amazons.objects.create(ward_id=ward)
        ama.save()
        return redirect('amazon-list')
    else:
        return redirect('amazon-list')

def amazons_edit(request, id):
    edit_name = Amazons.objects.get(id=id)
    # if request.method == "POST":
    if request.method == "GET":
        edit_name.name = request.POST.get("name")
        edit_name.save()
        # return redirect('amazon-list')
        return render(request, "Amazons_edit.html", context={"amazons": edit_name})
    else:
        return redirect('amazon-list')
    # if request.method == "POST":
        # import pdb; pdb.set_trace()
        # return render(request, "Amazons_edit.html", context={"amazons": edit_name})


def amazons_del(request, id):
    del_name = Amazons.objects.get(id=id)
    del_name.delete()
    return redirect('amazon-list')