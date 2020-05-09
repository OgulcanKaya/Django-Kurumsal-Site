from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from Home.models import UserProfile, Setting
from news.models import Category


def index(request):
    category = Category.objects.all()
    current_user = request.user
    profile = User.objects.get(pk=current_user.id)
    setting = Setting.objects.get(pk=1)
    context = {
        'category': category,
        'profile': profile,
        'setting': setting,
    }
    return render(request, 'userprofile.html', context)

def other_users(request,id):
    category = Category.objects.all()
    profile = User.objects.get(pk=id)
    setting = Setting.objects.get(pk=1)
    context = {
        'category': category,
        'setting': setting,
        'profile': profile,
    }
    return render(request, 'otheruserprofile.html', context)
