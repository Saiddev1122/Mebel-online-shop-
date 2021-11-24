from pyexpat import model

from django.db import models

# Create your models here.
from django.utils.text import slugify

from base.choices import default_price, default_size


class Category(models.Model):
    content = models.JSONField(default={"uz": "", "ru": ""})
    slug = models.SlugField(unique=True, max_length=256)
    is_active = models.BooleanField(default=True)
    is_main = models.BooleanField(default=True)

    def save(self, *args, **kwargs):
        if self.slug is None:
            self.slug = slugify(self.content["uz"])
        super(Category, self).save(*args, **kwargs)

    def __str__(self):
        return self.content["ru"]


class Product(models.Model):
    title = models.JSONField(default={"uz": "", "ru": ""})
    price = models.IntegerField()
    price_type = models.CharField(max_length=10, choices=default_price())
    is_active = models.BooleanField(default=True)
    size = models.JSONField(default=default_size())
    ctg = models.ForeignKey(Category, on_delete=models.CASCADE)


class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    image = models.ImageField(upload_to="image/")

    def __str__(self):
        return self.product.title['ru']
