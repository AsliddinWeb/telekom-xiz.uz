from django.db import models

class Category(models.Model):
    title = models.CharField(max_length=455)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name_plural = "Kategoriyalar"

class News(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=455)
    image = models.ImageField(upload_to='news')
    body = models.TextField()
    cap_body = models.TextField(null=True, blank=True)
    slug = models.SlugField(null=True, blank=True, unique=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-id']
        verbose_name_plural = "Yangiliklar"