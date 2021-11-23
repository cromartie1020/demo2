from django.shortcuts import render


def about(request):
    return render(request, 'demo2/about.html')


def home(request):
    return render(request, 'demo2/home.html')
