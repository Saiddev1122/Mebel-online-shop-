from django.urls import path

from mebel_site import views


app_name = "site"
urlpatterns = [
    path('', views.home, name='home'),
    path('category/<slug>/', views.category, name='category_one'),
    path('category/', views.category, name='category'),
    path('product/', views.product, name='product'),
    path('product/<int:pk>/', views.product, name='product_one')

]
