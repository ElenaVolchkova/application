from django.shortcuts import render
from mysite.athletes.models import Athletes


def athletes(request):
    objects_ath = Athletes.objects.all()
    return render(request, 'athletes.html', context={'athletes': objects_ath})


def athletes_plus(request):
    # print('athletes')
    # import pdb; pdb.set_trace()
    # return athletes(request)
    # pass
    my_objects = Athletes.objects.filter(default=True)
    return render(request, 'athletes/plus.html', context={'athletes': my_objects })