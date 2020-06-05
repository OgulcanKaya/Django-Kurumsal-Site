from django.contrib.auth.models import User
from django.db import models
from ckeditor.widgets import CKEditorWidget


# Create your models here.
from django.forms import ModelForm, TextInput
from django.urls import reverse
from django.utils.safestring import mark_safe
from ckeditor_uploader.fields import RichTextUploadingField
from mptt.fields import TreeForeignKey
from mptt.models import MPTTModel
from django.forms import TextInput, Select, FileInput, EmailInput, ModelForm


class Category(MPTTModel):
    STATUS =(

        ('True', 'Evet'),
        ('False', 'Hayır'),
    )
    title = models.CharField(max_length=200)
    description = models.CharField(max_length=200)
    keyword = models.CharField(max_length=200)
    image = models.ImageField(blank=True, upload_to='images/')
    status = models.CharField(max_length=10, choices=STATUS)
    slug = models.SlugField(null=False, unique=True)
    parent = TreeForeignKey('self', blank=True, null=True, related_name='children', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class MPTTMeta:
        order_insertion_by = ['title']

    def __str__(self):
        full_path = [self.title]
        k = self.parent
        while k is not None:
            full_path.append(k.title)
            k=k.parent
        return '->'.join(full_path[::-1])


    def image_tag(self):
        return mark_safe('<img src="{}" height="50"/>'.format(self.image.url))
    image_tag.short_description = 'Image'

    def get_absolute_url(self):
        return reverse('category_detail', kwargs={'slug': self.slug})


class News(models.Model):
    STATUS =(

        ('True', 'Evet'),
        ('False', 'Hayır'),
    )
    category = models.ForeignKey(Category, on_delete=models.CASCADE) #relations with Category
    user = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=150)
    description = models.CharField(max_length=200)
    keyword = models.CharField(max_length=200)
    image = models.ImageField(blank=True, upload_to='images/')
    detail = RichTextUploadingField()
    status = models.CharField(max_length=10, choices=STATUS)
    slug = models.SlugField(null=False, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def image_tag(self):
        return mark_safe('<img src="{}" height="40"/>'.format(self.image.url))
    image_tag.short_description = 'Image'

    def get_absolute_url(self):
        return reverse('news_detail', kwargs={'slug': self.slug})

class Images(models.Model):
    news = models.ForeignKey(News, on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    image = models.ImageField(blank=True , upload_to='images/')

    def __str__(self):
        return self.title

    def image_tag(self):
        return mark_safe('<img src="{}" height="50"/>'.format(self.image.url))
    image_tag.short_description = 'Image'


class NewsImageForm(ModelForm):
    class Meta:
        model = Images
        fields = ['title', 'image',]


class Comment(models.Model):
    STATUS =(

        ('New', 'Yeni'),
        ('True', 'Evet'),
        ('False', 'Hayır'),
    )
    news = models.ForeignKey(News, on_delete=models.CASCADE) #relations with News
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # relations with User
    subject = models.CharField(max_length=200)
    comment = models.CharField(max_length=200)
    rate = models.IntegerField(blank=True)
    status = models.CharField(max_length=10, choices=STATUS, default='New')
    ip = models.CharField(blank=True, max_length=30)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.subject

    def category(self):
        return self.news.category


#Kullanıcının yeni yorum eklemesi için kullanucağı form
class CommentForm(ModelForm):
        class Meta:
            model = Comment
            fields = ['subject', 'comment', 'rate']

#Kullanıcının yeni içerik girmesi için kullanucağı form
class NewsForm(ModelForm):
    class Meta:
        model = News
        fields = ('category', 'title', 'description', 'keyword', 'slug',  'image', 'detail',)
        widgets = {
            'category': Select(attrs={'class=form-control valid': 'input', 'placeholder': 'category'}),
            'title': TextInput(attrs={'class=form-control valid': 'input', 'placeholder': 'Title'}),
            'description': TextInput(attrs={'class=form-control valid': 'input', 'placeholder': 'Description'}),
            'keyword': TextInput(attrs={'class=form-control valid': 'input', 'placeholder': 'Keyword'}),
            'slug': TextInput(attrs={'class=form-control valid': 'input', 'placeholder': 'Slug'}),
            'image': FileInput(attrs={'class': 'input', 'placeholder': 'Image'}),
            'detail': CKEditorWidget(),

        }