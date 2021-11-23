from django.shortcuts import render


def about(request):
    return render(request, 'product/about.html')


def home(request):
    return render(request, 'product/home.html')
