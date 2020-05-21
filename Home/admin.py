from django.contrib import admin

# Register your models here.
from Home.models import Setting, ContactFormMassage, UserProfile, FAQ


class ContactFormMessageAdmin(admin.ModelAdmin):
    list_display = ['name', 'message', 'email', 'subject', 'status']
    list_filter = ['status']

class UserProfileFormAdmin(admin.ModelAdmin):
    list_display = ['user_name', 'first_name', 'adress', 'image_tag', 'phone', 'city', 'country']
    readonly_fields = ('image_tag',)
    list_filter = ['city', 'country']

class FAQAdmin(admin.ModelAdmin):
    list_display = ['ordernumber', 'question', 'answer', 'status',]
    list_filter = ['status']

admin.site.register(ContactFormMassage, ContactFormMessageAdmin)
admin.site.register(Setting)
admin.site.register(UserProfile, UserProfileFormAdmin)
admin.site.register(FAQ, FAQAdmin)