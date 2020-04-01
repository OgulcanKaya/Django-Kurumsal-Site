from django.contrib import admin

# Register your models here.
from news.models import Category, News


class CategoryAdmin(admin.ModelAdmin):
   # fields = ['title', 'status']   liste kısıtlama göstermek istenmeyenler için

    list_display = ['title', 'status']
    list_filter = ['status']
class NewsAdmin(admin.ModelAdmin):
   # fields = ['title', 'status']   liste kısıtlama göstermek istenmeyenler için

    list_display = ['title', 'category', 'status']
    list_filter = ['status','category']
admin.site.register(Category,CategoryAdmin)
admin.site.register(News,NewsAdmin)
