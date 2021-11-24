from django import forms

from mebel_site.models import ProductImage


class ProductImageForm(forms.ModelForm):
    class Meta:
        model = ProductImage
        exclude = ["slug"]
        fields = "__all__"
