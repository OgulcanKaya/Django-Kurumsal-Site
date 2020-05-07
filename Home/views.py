from django.contrib.auth import logout, authenticate, login
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.contrib import messages

# Create your views here.
from Home.forms import SearchForm, SignUpForm
from Home.models import Setting, ContactFormMassage, ContactFormu
from news.models import News, Category, Images, Comment
import json

def index(request):

    setting = Setting.objects.get(pk=1)
    setting2 = Setting.objects.get(pk=1)
    sliderdata = News.objects.all().order_by('?')[:8]
    category = Category.objects.all()
    daynews=News.objects.all().order_by('-id')[:8]
    randomnews = News.objects.all().order_by('?')[:8]
    comment = Comment.objects.all().order_by('-id')[:4]
    context = {'setting': setting,
               'category': category,
               'page': 'Home',
               'daynews': daynews,
               'randomnews': randomnews,
               'setting2': setting2,
               'sliderdata': sliderdata,
                'comment': comment}
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
    comment = Comment.objects.filter(news_id=id, status='True')
    context = {
        'news': news,
        'images': images,
        'category': category,
        'comment': comment,
    }
    return render(request, 'newsdetail.html', context)

def news_search(request):
    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            query = form.cleaned_data['query']
            category = Category.objects.all()
            catid = form.cleaned_data['catid']
            if catid == 0:
                news = News.objects.filter(title__icontains=query)
            else:
                news = News.objects.filter(title__icontains=query, category_id=catid)
            context = {
                'news': news,
                'category': category,
            }
            return render(request, 'news_search.html', context)

    return HttpResponseRedirect('/')

def news_search_auto(request):
    if request.is_ajax():
        q = request.GET.get('term', '')
        news = News.objects.filter(title__icontains=q)
        results = []
        for rs in news:
            news_json = {}
            news_json = rs.title
            results.append(news_json)
        data = json.dumps(results)
    else:
        data = 'fail'
    mimetype = 'application/json'
    return HttpResponse(data, mimetype)

def logout_view(request):
    logout(request)
    return HttpResponseRedirect('/')


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect('/')
        else:
            messages.warning(request, "Giriş Yapılamamıştır. Lütfen Kullanıcı Adı ve Şifrenizi Kontrol Ediniz!")
            return HttpResponseRedirect('/login')

    category = Category.objects.all()
    setting = Setting.objects.get(pk=1)
    context = {'category': category,
               'setting': setting,
               }
    return render(request, 'login.html', context)

def register_view(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = request.POST['username']
            password = request.POST['password1']
            user = authenticate(request, username=username, password=password)
            login(request, user)
            return HttpResponseRedirect('/')
    form = SignUpForm(request.POST)
    category = Category.objects.all()
    setting = Setting.objects.get(pk=1)
    context = {'category': category,
               'setting': setting,
               'form': form,
               }
    return render(request, 'register.html', context)