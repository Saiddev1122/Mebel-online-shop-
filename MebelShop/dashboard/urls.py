from django.urls import path, include

urlpatterns = [
    path('ctg/', include("dashboard.category.urls"), name="dashboard-category"),
    path('pro/', include("dashboard.product.urls"), name="dashboard-product"),
    path('proimg/', include("dashboard.productimage.urls"), name="dashboard-productimage"),
]
