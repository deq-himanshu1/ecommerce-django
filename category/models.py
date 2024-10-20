from django.db import models
from django.urls import reverse

# Create your models here.

class Category(models.Model):
    category_name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=100,unique=True) # it's a kind of url of the cagegory
    description = models.TextField(max_length=255,blank=True)
    cat_image = models.ImageField(upload_to='photos/categories',blank=True)

    class Meta:
        verbose_name = 'category'
        verbose_name_plural= 'categories'

    # This function will bring the urls of particular category
    def get_url(self):
        return reverse('products_by_category', args=[self.slug]) # 'products_by_category' --> taken from store app ---> urls.py

    # making string representation of the model
    def __str__(self):
        return self.category_name
