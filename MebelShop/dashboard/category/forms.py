from django import forms

from mebel_site.models import Category


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        exclude = ["slug"]
        fields = "__all__"
