from django.shortcuts import render


def index(request):
    return render(request, 'core/index.html', {})


def under_construction(request):
    return render(request, 'core/under_construction.html')
