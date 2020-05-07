from django.urls import path

from . import views

urlpatterns = [
    # ex: /Home/
    path('', views.index, name='index'),
    path('otherusers/<int:id>', views.other_users, name='other_users'),

    # ex: /polls/5/


]