from django.shortcuts import render

# Create your views here.
from mebel_site.models import Category, Product, ProductImage


def home(requests):
    ctg = Category.objects.all()
    pro = Product.objects.all()
    proimg = ProductImage.objects.all()
    ctx = {
        'ctg': ctg,
        'pro': pro,
        'proimg': proimg,
    }
    return render(requests, 'site/index.html')


def category(requests, slug=None):
    if slug:
        ctg_one = Category.objects.get(slug=slug)
        ctg = Category.objects.all()
        pro = Product.objects.all().filter(ctg_id=ctg_one.id)
        proimg = ProductImage.objects.all()
        ctx = {
            'ctg': ctg,
            'ctg_one': ctg_one,
            'pro': pro,
            'proimg': proimg,

        }
    else:
        ctx = {
            'ctg': Category.objects.all()
        }
    return render(requests, 'site/catalog.html', ctx)


def product(requests, pk=None):
    pro = Product.objects.all()
    pro_one = Product.objects.get(pk=pk)
    ctx = {
        'pro': pro,
        'pro_one': pro_one
    }
    return render(requests, 'site/product.html', ctx)
