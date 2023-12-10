from django.contrib import admin

from .models import *

admin.site.register(Category)

class NewsAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug', 'category', 'created_at']
    prepopulated_fields = {'slug': ('title', )}
admin.site.register(News, NewsAdmin)