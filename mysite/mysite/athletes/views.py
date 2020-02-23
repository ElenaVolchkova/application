from django.shortcuts import render
from mysite.athletes.models import Athletes


def athletes(request):
    objects_ath = Athletes.objects.all()
    return render(request, 'athletes.html', context={'athletes': objects_ath})
