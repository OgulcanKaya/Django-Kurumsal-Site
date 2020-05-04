
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.contrib import messages

# Create your views here.

from Home.models import Setting, ContactFormMassage, ContactFormu
from news.models import News, Category, Images


def index(request):

    setting = Setting.objects.get(pk=1)
    setting2 = Setting.objects.get(pk=1)
    sliderdata = News.objects.all()[:4]
    category = Category.objects.all()
    daynews=News.objects.all().order_by('-id')[:8]
    randomnews = News.objects.all().order_by('?')[:8]
    context = {'setting': setting,
               'category': category,
               'page': 'Home',
               'daynews': daynews,
               'randomnews': randomnews,
               'setting2': setting2,
               'sliderdata': sliderdata}
    return render(request, 'index.html', context)


def hakkimizda(request):
    category = Category.objects.all()
    setting = Setting.objects.get(pk=1)
    context = {'setting': setting,
               'category': category,
               }
    return render(request, 'hakkimizda.html', context)

def referanslar(request):
    category = Category.objects.all()
    setting = Setting.objects.get(pk=1)
    context = {'setting': setting,
               'category': category,
               }
    return render(request, 'referanslar.html', context)

def iletisim(request):

    if request.method == 'POST':
        form = ContactFormu(request.POST)
        if form.is_valid():
            data = ContactFormMassage()
            data.name = form.cleaned_data['name']
            data.email = form.cleaned_data['email']
            data.subject = form.cleaned_data['subject']
            data.message = form.cleaned_data['message']
            data.ip = request.META.get('REMOTE_ADDR')
            data.save()
            messages.success(request, "Mesajınız başarı ile gönderilmiştir. Teşekkür ederiz !")
            return HttpResponseRedirect ('/iletisim')


    setting = Setting.objects.get(pk=1)
    category = Category.objects.all()
    form =ContactFormu()
    context = {'setting': setting,
               'category': category,
               'form': form}
    return render(request, 'iletisim.html', context)

def category_news(request,id,slug):
    category = Category.objects.all()
    categorydata = Category.objects.get(pk=id)
    news = News.objects.filter(category_id = id)
    news2 = News.objects.all()
    context = {
            'news': news,
            'news2': news2,
            'category': category,
            'categorydata': categorydata,
             }
    return render(request, 'contents.html', context)

def news_detail(request,id,slug):
    category = Category.objects.all()
    news = News.objects.get(pk=id)
    images = Images.objects.filter(news_id=id)
    context = {
            'news': news,
            'images': images,
            'category': category,
             }
    return render(request, 'newsdetail.html', context)