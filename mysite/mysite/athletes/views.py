from django.shortcuts import render
from django.shortcuts import redirect
from mysite.athletes.models import Athletes


def athletes(request):
    objects_ath = Athletes.objects.all()
    return render(request, 'athletes.html', context={'athletes': objects_ath})


def athletes_plus(request):
    # athlete_id = int(request.POST.get("athlete_id"))
    # athlete = Athletes.objects.get(pk=athlete_id)
    # return redirect(athletes)
    pass
