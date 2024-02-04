from django.contrib import admin
from main import models


class PostView(admin.ModelAdmin):
    list_display = ['title','create_time','category','best']
    search_fields = ['title','body']
    list_filter = ['create_time','best']

class NewView(admin.ModelAdmin):
    list_display = ['text','create_time']
    search_fields = ['text']
    list_filter = ['create_time']



admin.site.register(models.Category)
admin.site.register(models.Post,PostView)
admin.site.register(models.New,NewView)
admin.site.register(models.Contact)