from django.shortcuts import render
from django.shortcuts import redirect
from mysite.amazons.models import Amazons


def amazons(request):
    ama = Amazons.objects.all()
    return render(request, 'amazons.html', context={'amazons': ama})


def amazons_plus(request):
    amazon_id = int(request.POST.get("amazon_id"))

    amazon = Amazons.objects.get(pk=amazon_id)

    amazon.month_1 = True
    amazon.save()
    return redirect('amazon-list')


# № тоже самое сделать для месяца и присваивать Екгу если месяц 1, 2,3... и т.д.
#     № проверить в РЕЬД почему не отрисовывает
#     № сделать, чтобы не добавляись снизу