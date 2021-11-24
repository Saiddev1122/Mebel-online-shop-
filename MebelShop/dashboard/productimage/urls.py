from . import views
from django.urls import path


urlpatterns = [
    path('list/', views.list_proimg, name="list_proimg"),
    path('form/', views.form_proimg, name="form_proimg"),
    path('detail/<int:pk>/', views.detail_proimg, name="detail_proimg"),
    path('delete/<int:pk>/', views.delete_proimg, name='delete_proimg'),
    path('edit/<int:pk>/', views.form_proimg, name='edit_proimg'),
]
