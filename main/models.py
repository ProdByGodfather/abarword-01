from django.db import models
from django.contrib.auth.models import User
from django_quill.fields import QuillField

class New(models.Model):
    text = models.TextField()
    create_time = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.text

class Category(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField(max_length=100)
    def __str__(self):
        return self.title

class Post(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField(null=True,blank=True)
    body = QuillField()
    image = models.ImageField(upload_to='users/%Y/%m/')
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    create_time = models.DateTimeField(auto_now=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    best = models.BooleanField(default=False)
    def __str__(self):
        return self.title
    
class Contact(models.Model):
    title = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    message = models.TextField()
    def __str__(self):
        return self.title

