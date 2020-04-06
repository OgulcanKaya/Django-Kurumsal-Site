from django.contrib import admin

# Register your models here.
from Home.models import Setting, ContactFormMassage

class ContactFormMessageAdmin(admin.ModelAdmin):
    list_display = ['name', 'message', 'email', 'subject', 'status']
    list_filter = ['status']


admin.site.register(ContactFormMassage, ContactFormMessageAdmin)
admin.site.register(Setting)