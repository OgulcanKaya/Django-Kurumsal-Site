from django.contrib import admin

# Register your models here.
from news.models import Category, News, Images


class NewsImageInline(admin.TabularInline):
    model = Images
    extra = 5

class CategoryAdmin(admin.ModelAdmin):
   # fields = ['title', 'status']   liste kısıtlama göstermek istenmeyenler için

    list_display = ['title', 'status']
    list_filter = ['status']


class NewsAdmin(admin.ModelAdmin):
   # fields = ['title', 'status']   liste kısıtlama göstermek istenmeyenler için

    list_display = ['title', 'category', 'status']
    list_filter = ['status', 'category']
    inlines = [NewsImageInline]


class ImagesAdmin(admin.ModelAdmin):
   # fields = ['title', 'status']   liste kısıtlama göstermek istenmeyenler için

    list_display = ['title', 'news', 'image']
    list_filter = ['news']




admin.site.register(Category, CategoryAdmin)
admin.site.register(News, NewsAdmin)
admin.site.register(Images, ImagesAdmin)
