from django.contrib import admin

from .models import *

class SeoSettingsAdmin(admin.ModelAdmin):
    list_display = ['keywords', 'description', 'author', 'favicon']
admin.site.register(SeoSettings, SeoSettingsAdmin)

class SiteSettingsAdmin(admin.ModelAdmin):
    list_display = ['title', 'logo']
admin.site.register(SiteSettings, SiteSettingsAdmin)

class OneHeaderAdmin(admin.ModelAdmin):
    list_display = ['title', 'link', 'is_submenu']
admin.site.register(OneHeader, OneHeaderAdmin)

class FooterSettingsAdmin(admin.ModelAdmin):
    list_display = ['title', 'cap_title', 'body', 'copyright']
admin.site.register(FooterSettings, FooterSettingsAdmin)

class FooterLinksAdmin(admin.ModelAdmin):
    list_display = ['title', 'link']
admin.site.register(FooterLinks, FooterLinksAdmin)

class FooterAddresInfoAdmin(admin.ModelAdmin):
    list_display = ['addres', 'phone', 'email']
admin.site.register(FooterAddresInfo, FooterAddresInfoAdmin)

class SocialNetworksAdmin(admin.ModelAdmin):
    list_display = ['title', 'icon', 'link']
admin.site.register(SocialNetworks, SocialNetworksAdmin)

admin.site.register(TelegramBotSettings)