from . import views
from django.urls import path


urlpatterns = [
    path('list/', views.list_pro, name="list_pro"),
    path('form/', views.form_pro, name="form_pro"),
    path('detail/<int:pk>/', views.detail_pro, name="detail_pro"),
    path('delete/<int:pk>/', views.delete_pro, name='delete_pro'),
    path('edit/<int:pk>/', views.form_pro, name='edit_pro'),
]
