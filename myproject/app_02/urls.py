from django.urls import path
from . import views

urlpatterns = [
    path('customers/', views.customer_list, name='customer_list'),
    path('products/', views.product_list, name='product_list'),
    path('orders/', views.order_list, name='order_list'),
    path('customer/create/', views.create_customer, name='create_customer'),
    path('product/create/', views.create_product, name='create_product'),
    path('customer/<int:pk>/update/', views.update_customer, name='update_customer'),
    path('product/<int:pk>/update/', views.update_product, name='update_product'),
    path('customer/<int:pk>/delete/', views.delete_customer, name='delete_customer'),
    path('product/<int:pk>/delete/', views.delete_product, name='delete_product'),
]
