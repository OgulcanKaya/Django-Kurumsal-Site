from django.urls import path

from . import views

urlpatterns = [
    # ex: /Home/
    path('', views.index, name='index'),
    # ex: /polls/5/
     path('addcomment/<int:id>/', views.addcomment, name='addcomment'),

]