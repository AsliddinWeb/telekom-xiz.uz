from django.db import models

class SeoSettings(models.Model):
    keywords = models.TextField()
    description = models.TextField()
    author = models.CharField(max_length=255)
    favicon = models.FileField(upload_to='favicons')

    def __str__(self):
        return self.author

class SiteSettings(models.Model):
    title = models.TextField()
    logo = models.ImageField(upload_to='logos')

    def __str__(self):
        return self.title

class OneHeader(models.Model):
    title = models.CharField(max_length=455)
    link = models.CharField(max_length=455, default="#")
    is_submenu = models.BooleanField(default=True)

    def __str__(self):
        return self.title

class FooterSettings(models.Model):
    cap_title = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    body = models.TextField()
    copyright = models.TextField()

    def __str__(self):
        return self.title

class FooterLinks(models.Model):
    title = models.CharField(max_length=255)
    link = models.CharField(max_length=255)

    def __str__(self):
        return self.title

class FooterAddresInfo(models.Model):
    addres = models.TextField()
    phone = models.CharField(max_length=255)
    email = models.CharField(max_length=255)

class SocialNetworks(models.Model):
    title = models.CharField(max_length=255)
    icon = models.CharField(max_length=255)
    link = models.CharField(max_length=255)

    def __str__(self):
        return self.title

class TelegramBotSettings(models.Model):
    username = models.CharField(max_length=455)
    token = models.CharField(max_length=555)
    user_id = models.CharField(max_length=255)

    def __str__(self):
        return self.username
