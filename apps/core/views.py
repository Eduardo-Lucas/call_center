from django.contrib.auth.decorators import login_required
from django.shortcuts import render


@login_required
def index(request):
    return render(request, 'core/index.html', {})


def precos(request):
    return render(request, 'core/precos.html', {})


def under_construction(request):
    return render(request, 'core/under_construction.html')
