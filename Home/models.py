from ckeditor_uploader.fields import RichTextUploadingField
from django.db import models
from django.forms import ModelForm, TextInput, Textarea


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