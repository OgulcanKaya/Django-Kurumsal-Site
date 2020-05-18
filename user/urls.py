from django.urls import path

from . import views

urlpatterns = [
    # ex: /Home/
    path('', views.index, name='index'),
    path('otherusers/<int:id>', views.other_users, name='other_users'),
    path('update/', views.user_update, name='user_update'),
    path('password/', views.change_password, name='change_password'),

    # ex: /polls/5/


]