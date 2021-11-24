from django.urls import path
from . import views

urlpatterns = [
    path('list/', views.list_ctg, name="list_ctg"),
    path('form/', views.form_ctg, name="form_ctg"),
    path('detail/<int:pk>/', views.detail_ctg, name="detail_ctg"),
    path('delete/<int:pk>/', views.delete_ctg, name='delete_ctg'),
    path('edit/<int:pk>/', views.form_ctg, name='edit_ctg'),
]
