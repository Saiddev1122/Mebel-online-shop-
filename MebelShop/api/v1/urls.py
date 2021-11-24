from django.urls import path

from .Category import views as ctg_view
from .Product import views as pro_view
from .ProductImage import views as proimg_view

urlpatterns = [
    path('category/', ctg_view.CategoryView.as_view(), name="category_list"),
    path('category/<int:pk>/', ctg_view.CategoryView.as_view(), name="category_one"),
    path('product/', pro_view.ProductView.as_view(), name="product_list"),
    path('product/<int:pk>/', pro_view.ProductView.as_view(), name="product_one"),
    path('productimage/', proimg_view.ProductImageView.as_view(), name="productimg_list"),
    path('productimage/<int:pk>/', proimg_view.ProductImageView.as_view(), name="productimg_one"),
]
