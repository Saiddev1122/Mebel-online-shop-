from django.contrib import admin

# Register your models here.
from mebel_site.models import ProductImage, Product, Category


class ProductImageAdmin(admin.StackedInline):
    model = ProductImage


class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductImageAdmin]

    class Meta:
        model = Product


admin.site.register(Product, ProductAdmin)
admin.site.register(Category)
admin.site.register(ProductImage)
