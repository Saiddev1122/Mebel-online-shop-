from django.shortcuts import render, redirect

from dashboard.product.forms import ProductForm
from mebel_site.models import Product


def list_pro(requests):
    all = Product.objects.all()
    print(all)
    ctx = {
        "all": all
    }
    return render(requests, "dashboard/product/list.html", ctx)


def form_pro(requestes, pk=None):
    if pk:
        edit_one = Product.objects.get(pk=pk)
        edit = True
        form = ProductForm(requestes.POST or None, requestes.FILES or None, instance=edit_one)
        if form.is_valid():
            form.save()
        ctx = {
            "edit_one": edit_one,
            "form": form
        }
    else:
        form = ProductForm()
        if requestes.POST:
            forms = ProductForm(requestes.POST or None, requestes.FILES or None)
            if forms.is_valid():
                forms.save()
        ctx = {
            'form': form
        }
    return render(requestes, 'dashboard/product/form.html', ctx)


def detail_pro(requests, pk=None):
    one = Product.objects.get(pk=pk)
    ctx = {
        "one": one
    }
    return render(requests, "dashboard/product/detail.html", ctx)


def delete_pro(requestes, pk):
    delate_one = Product.objects.get(pk=pk)
    delate_one.delete()
    return redirect('list_pro')
