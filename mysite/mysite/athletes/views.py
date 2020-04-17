from django.shortcuts import render
from django.shortcuts import redirect
from mysite.athletes.models import Athletes
from mysite.ward.models import Ward


def athletes(request):
    objects_ath = Athletes.objects.all()
    return render(request, 'athletes.html', context={'athletes': objects_ath})


def athletes_plus(request):
    athlete_id = int(request.POST.get("athlete_id"))
    athlete = Athletes.objects.get(pk=athlete_id)
    month_id = int(request.POST.get("month_id"))
    months = Athletes.objects.get(pk=month_id)
    for month in months:
        if month == True:
            athlete.save()
    return redirect('athlete-list')

def athletes_new(request):
    name = request.POST.get("name")
    if name not in [x.ward for x in Ward.objects.all()]:
        ward = Ward.objects.create(ward=name)
        ward.save()
        objects_ath = Athletes.objects.create(ward_id=ward)
        objects_ath.save()
        return redirect('athlete-list')
    else:
        return redirect('athlete-list')


# def athletes_update(request, id):
#     edit_name = Athletes.objects.get(id=id)
#     if request.method == "GET":
#         edit_name.name = request.POST.get("name")
#         edit_name.save()
#         return redirect('athlete-list')


def athletes_edit(request, id):
    edit_name = Athletes.objects.get(id=id)
    # if request.method == "POST":
    if request.method == "GET":
        edit_name.name = request.POST.get("name")
        edit_name.save()
        # return redirect('athlete-list')
        return render(request, "Athlete_edit.html", context={"athletes": edit_name})
    else:
        return redirect('athlete-list')
    # if request.method == "POST":
        # import pdb; pdb.set_trace()
        # return render(request, "Athlete_edit.html", context={"athletes": edit_name})


def athletes_del(request, id):
    del_name = Athletes.objects.get(id=id)
    del_name.delete()
    return redirect('athlete-list')
