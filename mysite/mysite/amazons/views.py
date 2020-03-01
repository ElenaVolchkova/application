from django.shortcuts import render
from mysite.amazons.models import Amazons


def amazons(request):
    ama = Amazons.objects.all()
    return render(request, 'amazons.html', context={'amazons': ama})


def amazons_plus(request):
    # plus = Amazons.objects.all()
    # print(plus)
    # import pdb; pdb.set_trace()
    # return render(request, 'amazons/plus.html', context={'amazons': plus})
    # return amazons(request)
    my_objects = Amazons.objects.filter(default=True)
    return render(request, 'amazons/plus.html', context={'amazons': my_objects })
