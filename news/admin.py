from django.contrib import admin

# Register your models here.
from news.models import category

class categoryAdmin(admin.ModelAdmin):
   # fields = ['title', 'status']   liste kısıtlama göstermek istenmeyenler için

    list_display = ['title', 'status']
    list_filter = ['status']

admin.site.register(category,categoryAdmin)
