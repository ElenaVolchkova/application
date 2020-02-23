from django.shortcuts import render
from mysite.amazons.models import Amazons


def amazons(request):
    ama = Amazons.objects.all()
    return render(request, 'amazons.html', context={'amazons': ama})
