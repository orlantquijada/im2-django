from django.shortcuts import render


def main_view(request):
    return render(request, 'main/index.html')


def main_view2(request):
    return render(request, 'main/index2.html')
