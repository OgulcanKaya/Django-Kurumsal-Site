from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from Home import views


urlpatterns = [
    path('', include('Home.urls')),
    path('home/', include('Home.urls')),
    path('news/', include('news.urls')),
    path('admin/', admin.site.urls),
    path('user/', include('user.urls')),
    path('ckeditor/', include('ckeditor_uploader.urls')),


    path('hakkimizda', views.hakkimizda, name='hakkimizda'),
    path('referanslar', views.referanslar, name='referanslar'),
    path('iletisim', views.iletisim, name='iletisim'),
    path('category/<int:id>/<slug:slug>/', views.category_news, name='category_news'),
    path('news/<int:id>/<slug:slug>/', views.news_detail, name='news_detail'),
    path('SSS/', views.faq, name='faq'),


    path('search/', views.news_search, name='news_search'),
    path('search_auto/', views.news_search_auto, name='news_search_auto'),
    path('logout/', views.logout_view, name='logout_view'),
    path('login/', views.login_view, name='login_view'),
    path('register/', views.register_view, name='register_view'),




]
if settings.DEBUG: # new
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
