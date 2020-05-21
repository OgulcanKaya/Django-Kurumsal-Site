from django.urls import path

from . import views

urlpatterns = [
    # ex: /Home/
    path('', views.index, name='index'),
    path('otherusers/<int:id>', views.other_users, name='other_users'),
    path('update/', views.user_update, name='user_update'),
    path('password/', views.change_password, name='change_password'),
    path('comments/', views.comments, name='comments'),
    path('deletecomment/<int:id>', views.delete_comment, name='delete_comment'),
    path('addnews/', views.add_news, name='add_news'),
    path('mynews/', views.my_news, name='my_news'),
    path('news_edit/<int:id>', views.news_edit, name='news_edit'),
    path('news_delete/<int:id>', views.news_delete, name='news_delete'),
    path('newsaddimage/<int:id>', views.news_add_image, name='news_add_image'),
    # ex: /polls/5/


]