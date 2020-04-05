from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from Home.models import Setting


def index(request):

    setting = Setting.objects.get(pk=1)
    context = {'setting': setting, 'page':'Home'}
    return render(request, 'index.html', context)


def hakkimizda(request):

    setting = Setting.objects.get(pk=1)
    context = {'setting': setting}
    return render(request, 'hakkimizda.html', context)

def referanslar(request):

    setting = Setting.objects.get(pk=1)
    context = {'setting': setting}
    return render(request, 'referanslar.html', context)

def iletisim(request):

    setting = Setting.objects.get(pk=1)
    context = {'setting': setting}
    return render(request, 'iletisim.html', context)