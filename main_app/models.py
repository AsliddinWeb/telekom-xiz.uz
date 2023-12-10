from django.db import models

class HomeWelcome(models.Model):
    image1 = models.ImageField(upload_to='home-images')
    image2 = models.ImageField(upload_to='home-images')

    cap_title = models.CharField(max_length=455)
    title = models.CharField(max_length=455)
    body = models.TextField()

    button_title = models.CharField(max_length=455)
    button_link = models.CharField(max_length=455)

    def __str__(self):
        return self.title

class HomeIqtibos(models.Model):
    title = models.TextField()
    author = models.CharField(max_length=455)

    def __str__(self):
        return self.title

class HomeStep(models.Model):
    title = models.CharField(max_length=255)
    body = models.TextField()

    image_1 = models.ImageField(upload_to='home-images')
    text_1 = models.CharField(max_length=455)

    image_2 = models.ImageField(upload_to='home-images')
    text_2 = models.CharField(max_length=455)

    image_3 = models.ImageField(upload_to='home-images')
    text_3 = models.CharField(max_length=455)

    image_4 = models.ImageField(upload_to='home-images')
    text_4 = models.CharField(max_length=455)

    def __str__(self):
        return self.title

class HomeSerives(models.Model):
    title = models.CharField(max_length=455)
    icon = models.CharField(max_length=255)
    body = models.TextField()

    animation = models.CharField(max_length=255, null=True, blank=True)
    animation_delay = models.CharField(max_length=255, null=True, blank=True)

    slug = models.CharField(max_length=455)
    status = models.BooleanField(default=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class HomeCounter(models.Model):
    title = models.CharField(max_length=455)
    icon = models.CharField(max_length=455)
    count = models.CharField(max_length=255)
    aniq = models.BooleanField(default=False)

    def __str__(self):
        return self.title

class HomeHamkor(models.Model):
    title = models.CharField(max_length=255)
    image = models.ImageField(upload_to='home-images')
    link = models.CharField(max_length=455)

    def __str__(self):
        return self.title

# --------------------------------------- Contact Page -----------------------
class ContactInfo(models.Model):
    title = models.CharField(max_length=455)
    cap_title = models.CharField(max_length=455)
    body = models.TextField()

    adress = models.CharField(max_length=455)
    phone = models.CharField(max_length=455)
    email = models.CharField(max_length=455)

    def __str__(self):
        return self.title

class ContactRequests(models.Model):
    name = models.CharField(max_length=455)
    phone = models.CharField(max_length=455)
    message = models.TextField()

    def __str__(self):
        return self.name
