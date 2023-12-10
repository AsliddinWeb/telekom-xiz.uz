from django.contrib import admin

from .models import *

class HomeWelcomeAdmin(admin.ModelAdmin):
    list_display = ['title', 'cap_title', 'image1', 'image2', 'body', 'button_title', 'button_link']
admin.site.register(HomeWelcome, HomeWelcomeAdmin)

class HomeIqtibosAdmin(admin.ModelAdmin):
    list_display = ['title', 'author']
admin.site.register(HomeIqtibos, HomeIqtibosAdmin)

class HomeStepAdmin(admin.ModelAdmin):
    list_display = ['title', 'body', 'image_1', 'text_1', 'image_2', 'text_2', 'image_3', 'text_3', 'image_4', 'text_4']
admin.site.register(HomeStep, HomeStepAdmin)

class HomeSerivesAdmin(admin.ModelAdmin):
    list_display = ['title', 'icon', 'body', 'slug', 'status', 'created_at', 'updated_at']
admin.site.register(HomeSerives, HomeSerivesAdmin)

class HomeCounterAdmin(admin.ModelAdmin):
    list_display = ['title', 'icon', 'count', 'aniq']
admin.site.register(HomeCounter, HomeCounterAdmin)

class HomeHamkorAdmin(admin.ModelAdmin):
    list_display = ['title', 'image', 'link']
admin.site.register(HomeHamkor, HomeHamkorAdmin)


admin.site.register(ContactInfo)
admin.site.register(ContactRequests)