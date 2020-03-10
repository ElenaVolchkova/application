from django.shortcuts import render
from django.shortcuts import redirect
from mysite.athletes.models import Athletes


def athletes(request):
    objects_ath = Athletes.objects.all()
    return render(request, 'athletes.html', context={'athletes': objects_ath})


def athletes_plus(request):
    athlete_id = int(request.POST.get("athlete_id"))
    athlete = Athletes.objects.get(pk=athlete_id)
    months = [athlete.month_1, athlete.month_2, athlete.month_3, athlete.month_4]
    for month in months:
        if month == True:
            athlete.save()
    return redirect('athlete-list')
