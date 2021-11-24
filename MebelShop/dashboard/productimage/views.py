from django.shortcuts import render, redirect

from dashboard.productimage.forms import ProductImageForm
from mebel_site.models import ProductImage


def list_proimg(requests):
    all = ProductImage.objects.all()
    print(all)
    ctx = {
        "all": all
    }
    return render(requests, "dashboard/productimage/list.html", ctx)


def form_proimg(requestes, pk=None):
    if pk:
        edit_one = ProductImage.objects.get(pk=pk)
        edit = True
        form = ProductImageForm(requestes.POST or None, requestes.FILES or None, instance=edit_one)
        if form.is_valid():
            form.save()
        ctx = {
            "edit_one": edit_one,
            "form": form
        }
    else:
        form = ProductImageForm()
        if requestes.POST:
            forms = ProductImageForm(requestes.POST or None, requestes.FILES or None)
            if forms.is_valid():
                forms.save()
        ctx = {
            'form': form
        }
    return render(requestes, 'dashboard/productimage/form.html', ctx)


def detail_proimg(requests, pk=None):
    one = ProductImage.objects.get(pk=pk)
    ctx = {
        "one": one
    }
    return render(requests, "dashboard/productimage/detail.html", ctx)


def delete_proimg(requestes, pk):
    delate_one = ProductImage.objects.get(pk=pk)
    delate_one.delete()
    return redirect('list_proimg')
