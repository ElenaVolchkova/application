from django.shortcuts import render


def ward(request):
    return render(request, 'ward.html')
