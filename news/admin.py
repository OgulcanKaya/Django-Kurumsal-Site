from django.contrib import admin

# Register your models here.
from django.utils.html import format_html
from mptt.admin import MPTTModelAdmin, DraggableMPTTAdmin

from news.models import Category, News, Images, Comment


class NewsImageInline(admin.TabularInline):
    model = Images
    extra = 5

class CategoryAdmin(admin.ModelAdmin):
    # fields = ['title', 'status']   liste kısıtlama göstermek istenmeyenler için

    list_display = ['title', 'status', 'image_tag']
    readonly_fields = ('image_tag',)
    list_filter = ['status']


class NewsAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'status', 'image_tag', 'slug',]
    readonly_fields = ('image_tag',)
    list_filter = ['status', 'category']
    prepopulated_fields = {'slug': ('title',)}
    inlines = [NewsImageInline]



class ImagesAdmin(admin.ModelAdmin):
    list_display = ['title', 'news', 'image_tag']
    readonly_fields = ('image_tag',)
    list_filter = ['news']

class CategoryAdmin2(DraggableMPTTAdmin):
    mptt_indent_field = "title"
    list_display = ('tree_actions', 'indented_title',
                    'related_news_count', 'related_news_cumulative_count')
    list_display_links = ('indented_title',)
    prepopulated_fields = {'slug' : ('title',)}

    def get_queryset(self, request):
        qs = super().get_queryset(request)

        # Add cumulative product count
        qs = Category.objects.add_related_count(
                qs,
                News,
                'category',
                'news_cumulative_count',
                cumulative=True)

        # Add non cumulative product count
        qs = Category.objects.add_related_count(qs,
                 News,
                 'category',
                 'news_count',
                 cumulative=False)
        return qs

    def related_news_count(self, instance):
        return instance.news_count
    related_news_count.short_description = 'Related news (for this specific category)'

    def related_news_cumulative_count(self, instance):
        return instance.news_cumulative_count
    related_news_cumulative_count.short_description = 'Related news (in tree)'

class CommentAdmin(admin.ModelAdmin):
    list_display = ['subject', 'comment', 'news', 'user', 'status']
    list_filter = ['status']




admin.site.register(Category, CategoryAdmin2)
admin.site.register(News, NewsAdmin)
admin.site.register(Images, ImagesAdmin)
admin.site.register(Comment, CommentAdmin)