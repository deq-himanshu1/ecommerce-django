from django.db import models
from category.models import Category
from django.urls import reverse

# Create your models here.
class Product(models.Model):
    product_name        = models.CharField(max_length=200, unique=True)
    slug                = models.SlugField(max_length=200, unique=True)
    description         = models.TextField(max_length=500, blank=True)
    price               = models.IntegerField()
    images              = models.ImageField(upload_to='photos/products')
    stock               = models.IntegerField()
    is_available        = models.BooleanField(default=True)
    category            = models.ForeignKey(Category, on_delete=models.CASCADE) # the variable category is the foreign key, on_delete=models.cascade means 
                                                                # if we delete category form Cateory model so the all product related to that category will be deleted 
    created_date        = models.DateTimeField(auto_now_add=True)
    modified_date       = models.DateTimeField(auto_now=True)

    def get_url(self):
        return reverse('product_detail', args=[self.category.slug, self.slug]) # 'products_by_category' --> taken from store app ---> urls.py

    def __str__(self):
        return self.product_name                                                                     