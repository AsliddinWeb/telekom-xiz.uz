from django.contrib import admin

from .models import *

admin.site.register(ServiceCategory)

class ServicesAdmin(admin.ModelAdmin):
    list_display = ['title', 'image', 'body', 'category', 'slug']
    prepopulated_fields = {'slug': ('title', )}
admin.site.register(Services, ServicesAdmin)

class ServiceOrderAdmin(admin.ModelAdmin):
    list_display = ['id', 'service', 'status', 'created_at']
admin.site.register(ServiceOrder, ServiceOrderAdmin)