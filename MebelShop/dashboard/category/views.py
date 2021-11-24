from django.shortcuts import render, redirect

from dashboard.category.forms import CategoryForm
from mebel_site.models import Category


def list_ctg(requests):
    all = Category.objects.all()
    print(all)
    ctx = {
        "all": all
    }
    return render(requests, "dashboard/category/list.html", ctx)


def form_ctg(requestes, pk=None):
    if pk:
        edit_one = Category.objects.get(pk=pk)
        edit = True
        form = CategoryForm(requestes.POST or None, requestes.FILES or None, instance=edit_one)
        if form.is_valid():
            form.save()
        ctx = {
            "edit_one": edit_one,
            "form": form
        }
    else:
        form = CategoryForm()
        if requestes.POST:
            forms = CategoryForm(requestes.POST or None, requestes.FILES or None)
            if forms.is_valid():
                forms.save()
        ctx = {
            'form': form
        }
    return render(requestes, 'dashboard/category/form.html', ctx)


def detail_ctg(requests, pk=None):
    one = Category.objects.get(pk=pk)
    ctx = {
        "one": one
    }
    return render(requests, "dashboard/category/detail.html", ctx)


def delete_ctg(requestes, pk):
    delate_one = Category.objects.get(pk=pk)
    delate_one.delete()
    return redirect('list_ctg')


