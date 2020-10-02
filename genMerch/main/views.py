from django.shortcuts import render, redirect


def main_view(request):
    return render(request, "main/index.html")


def redirect_home(request):
    return redirect("main:main")
