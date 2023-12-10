from django.db import models

class ServiceCategory(models.Model):
    title = models.CharField(max_length=455)

    def __str__(self):
        return self.title

class Services(models.Model):
    title = models.CharField(max_length=455)
    image = models.ImageField(upload_to='services')
    body = models.TextField()
    category = models.ForeignKey(ServiceCategory, on_delete=models.CASCADE)
    slug = models.SlugField(max_length=455, null=True, blank=True)

    author = models.CharField(max_length=255)
    author_site = models.CharField(max_length=255)
    author_image = models.ImageField(upload_to='authors')
    author_body = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

STATUS_CHOICES = (
    ('1', "Qabul qilindi"),
    ('2', "Bajarildi"),
    ('3', "Bekor qilindi"),
)
class ServiceOrder(models.Model):
    service = models.ForeignKey(Services, on_delete=models.CASCADE)

    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=255)
    address = models.CharField(max_length=255)

    status = models.CharField(max_length=255, choices=STATUS_CHOICES, default='1')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.service.title
