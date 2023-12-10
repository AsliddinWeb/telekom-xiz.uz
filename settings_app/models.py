from django.db import models

class SeoSettings(models.Model):
    keywords = models.TextField()
    description = models.TextField()
    author = models.CharField(max_length=255)
    favicon = models.FileField(upload_to='favicons')

    def __str__(self):
        return self.author

    class Meta:
        verbose_name_plural = "Seo sozlamalari"

class SiteSettings(models.Model):
    title = models.TextField()
    logo = models.ImageField(upload_to='logos')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Logo va title sozlamalari"

class OneHeader(models.Model):
    title = models.CharField(max_length=455)
    link = models.CharField(max_length=455, default="#")
    is_submenu = models.BooleanField(default=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Asosiy menyular"

class FooterSettings(models.Model):
    cap_title = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    body = models.TextField()
    copyright = models.TextField()

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Footer sozlamalari"

class FooterLinks(models.Model):
    title = models.CharField(max_length=255)
    link = models.CharField(max_length=255)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Footer linklar"

class FooterAddresInfo(models.Model):
    addres = models.TextField()
    phone = models.CharField(max_length=255)
    email = models.CharField(max_length=255)

    class Meta:
        verbose_name_plural = "Footer manzil sozlamalari"

class SocialNetworks(models.Model):
    title = models.CharField(max_length=255)
    icon = models.CharField(max_length=255)
    link = models.CharField(max_length=255)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Ijtimoiy tarmoqlar"

class TelegramBotSettings(models.Model):
    username = models.CharField(max_length=455)
    token = models.CharField(max_length=555)
    user_id = models.CharField(max_length=255)

    def __str__(self):
        return self.username

    class Meta:
        verbose_name_plural = "Telegram bot sozlamalari"