from django.urls import path
from . import views

urlpatterns = [
    path('product/insert/', views.product_insert, name='product_insert'),
    path('product/list/', views.product_list, name='product_list'),
    path('product/<int:product_id>/', views.product_info, name='product_info'),
    path('product/<int:product_id>/edit_inventory/', views.product_editInventory, name='product_editInventory'),
    path('accounts/customer/register/', views.customer_register, name='customer_register'),
    path('accounts/customer/list/', views.customer_list, name='customer_list'),
    path('accounts/customer/<int:customer_id>/', views.customer_info, name='customer_info'),
    path('accounts/customer/<int:customer_id>/edit/', views.customer_edit, name='customer_edit'),
    path('accounts/customer/login/', views.customer_login, name='customer_login'),
    path('accounts/customer/logout/', views.customer_logout, name='customer_logout'),
    path('accounts/customer/profile/', views.customer_profile, name='customer_profile'),
    path('shopping/cart/', views.shopping_cart, name='shopping_cart'),
    path('shopping/cart/add_items/', views.shopping_add_items, name='shopping_add_items'),
    path('shopping/cart/remove_items/', views.shopping_remove_items, name='shopping_remove_items'),
    path('shopping/submit/', views.shopping_submit, name='shopping_submit'),
]
