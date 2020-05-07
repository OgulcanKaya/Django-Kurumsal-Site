from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from Home.models import UserProfile
from news.models import Category


def index(request):
    category = Category.objects.all()
    current_user = request.user
    profile = UserProfile.objects.get(user_id=current_user.id)
    context = {
               'category': category,
               'profile': profile,
               }
    return render(request, 'userprofile.html', context)

def other_users(request,id):
    category = Category.objects.all()
    profile = User.objects.get(pk=id)
    context = {
               'category': category,
               'profile': profile,
               }
    return render(request, 'otheruserprofile.html', context)
