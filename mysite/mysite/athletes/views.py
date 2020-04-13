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
