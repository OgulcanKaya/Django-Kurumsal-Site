from ckeditor_uploader.fields import RichTextUploadingField
from django.contrib.auth.models import User
from django.db import models
from django.forms import ModelForm, TextInput, Textarea
from django.utils.safestring import mark_safe


class Setting(models.Model):
    STATUS =(

        ('True', 'Evet'),
        ('False', 'Hayır'),
    )

    title = models.CharField(max_length=150)
    keywords = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    company = models.CharField(max_length=50)
    address = models.CharField(blank=True, max_length=150)
    phone = models.CharField(blank=True,max_length=15)
    fax = models.CharField(blank=True, max_length=15)
    email = models.CharField(blank=True, max_length=50)
    map = models.TextField(blank=True)
    smtpserver = models.CharField(blank=True, max_length=20)
    smtpemail = models.CharField(blank=True, max_length=20)
    smtppassword = models.CharField(blank=True, max_length=20)
    smtpport = models.CharField(blank=True, max_length=5)
    icon = models.ImageField(blank=True, upload_to='images/')
    facebook = models.CharField(max_length=50)
    twitter = models.CharField(max_length=50)
    instagram = models.CharField(max_length=50)
    aboutus = RichTextUploadingField(blank=True)
    contactus = RichTextUploadingField(blank=True)
    references = RichTextUploadingField(blank=True)
    status = models.CharField(max_length=10, choices=STATUS)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.title

class ContactFormMassage(models.Model):

        STATUS = (

            ('New', 'New'),
            ('Read', 'Read'),
            ('Closed', 'Closed'),
        )
        name = models.CharField(max_length=150)
        email = models.CharField(max_length=200)
        subject = models.CharField(max_length=200)
        message = models.CharField(max_length=50)
        status = models.CharField(max_length=10, choices= STATUS)
        ip = models.CharField(blank=True, max_length=15)
        note = models.CharField(blank=True, max_length=15)
        created_at = models.DateTimeField(auto_now_add=True)
        updated_at = models.DateTimeField(auto_now=True)

        def __str__(self):
            return self.name


class ContactFormu(ModelForm):
    class Meta:
        model = ContactFormMassage
        fields = ['name', 'email', 'subject', 'message']
        widgets = {
            'name'  : TextInput(attrs={'class': 'input', 'placeholder' : 'Name & Surname'}),
            'subject'  : TextInput(attrs={'class': 'input', 'placeholder' : 'Subject'}),
            'email'  : TextInput(attrs={'class': 'input', 'placeholder' : 'Email Adress'}),
            'message'  : Textarea(attrs={'class': 'input', 'placeholder' : 'Your Message', 'rows': '5'}),
        }

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=15)
    adress = models.CharField(max_length=150)
    city = models.CharField(max_length=150)
    country = models.CharField(max_length=150)
    image = models.ImageField(blank=True, upload_to='images/users/')

    def __str__(self):
        return self.user.username

    def user_name(self):
        return '[' + self.user.username + ']'

    def first_name(self):
        return self.user.first_name + ' ' + self.user.last_name

    def image_tag(self):
        return mark_safe('<img src="{}" height="50"/>'.format(self.image.url))

    image_tag.short_description = 'Image'

class UserProfileForm(ModelForm):
    class Meta:
        model = UserProfile
        fields = ['phone', 'adress', 'city', 'country', 'image']


#***********************sıkça sorular sorular*****************
class FAQ(models.Model):
    STATUS =(

        ('True', 'Evet'),
        ('False', 'Hayır'),
    )

    ordernumber = models.IntegerField()
    question = models.CharField(max_length=150)
    answer = models.TextField()
    status = models.CharField(max_length=10, choices=STATUS)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    def __str__(self):
        return self.question