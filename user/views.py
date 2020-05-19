from django.contrib import messages
from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth.models import User
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect

# Create your views here.
from Home.models import UserProfile, Setting
from news.models import Category, Comment
from user.forms import UserUpdateForm, ProfileUpdateForm

@login_required(login_url='/login')
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

@login_required(login_url='/login')
def user_update(request):
    if request.method == 'POST':
        user_form = UserUpdateForm(request.POST, instance=request.user)
        profile_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.userprofile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Your account has been updated')
            return redirect('/user')
    else:
        category = Category.objects.all()
        current_user = request.user
        user_form = UserUpdateForm(instance=request.user)
        profile_form = ProfileUpdateForm(instance=request.user.userprofile)
        profile = User.objects.get(pk=current_user.id)
        setting = Setting.objects.get(pk=1)
        context = {
        'category': category,
        'user_form': user_form,
        'profile_form': profile_form,
        'profile': profile,
        'setting': setting,
        }
        return render(request, 'user_update.html', context)

@login_required(login_url='/login')
def change_password(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            messages.success(request, 'Your password has been changed')
            return HttpResponseRedirect('/user')
        else:
            messages.error(request, 'Please correct the error bellow.<br>' + str(form.errors))
            return HttpResponseRedirect('/user/password')
    else:
        category = Category.objects.all()
        form = PasswordChangeForm(request.user)
        setting = Setting.objects.get(pk=1)
        context = {
        'category': category,
        'form': form,
        'setting': setting,
        }
        return render(request, 'change_password.html', context)

@login_required(login_url='/login')
def comments(request):
    category = Category.objects.all()
    current_user = request.user
    comments = Comment.objects.filter(user_id=current_user.id)
    profile = User.objects.get(pk=current_user.id)
    setting = Setting.objects.get(pk=1)
    context = {
        'category': category,
        'comments': comments,
        'setting': setting,
        'profile': profile,
    }
    return render(request, 'user_comments.html', context)

@login_required(login_url='/login')
def delete_comment(request, id):
    current_user = request.user
    Comment.objects.filter(id=id, user_id=current_user.id).delete()
    messages.success(request, 'Your comments has been deleted successfuly.')
    return HttpResponseRedirect('/user/comments')