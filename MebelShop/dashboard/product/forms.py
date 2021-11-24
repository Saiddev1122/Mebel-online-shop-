from django import forms

from mebel_site.models import Product


class ProductForm(forms.ModelForm):
    class Meta:
        model = Product
        exclude = ["slug"]
        fields = "__all__"
