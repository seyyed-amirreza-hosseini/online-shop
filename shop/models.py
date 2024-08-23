from django.db import models
from django.urls import reverse


class Category(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True)

    class Meta:
        ordering = ['title']
        indexes = [
            models.Index(fields=['title']),
        ]
        verbose_name = 'category'
        verbose_name_plural = 'categories'

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("shop:product_list_by_category", args=[self.slug])
        


class Product(models.Model):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='products/%Y/%m/%d', blank=True)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    available = models.BooleanField(default=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


    class Meta:
        indexes = [
            models.Index(fields=['id', 'slug']),
            models.Index(fields=['title']),
            models.Index(fields=['-created']),
        ]   

    def __str__(self):
        return self.title    
    
    def get_absolute_url(self):
        return reverse("shop:product_detail", args=[self.id, self.slug])
    