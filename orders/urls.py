from django.urls import path

from . import views

urlpatterns = [
    path('orders/', views.get_order_api, name="orders"),
    path('orders/<int:id>/', views.get_order_api, name="one-order"),
    path('orders/create/', views.add_order_api, name='create-order'),
    path('orders/update/<int:id>/', views.update_order_api, name='order-update'),
    path('orders/delete/<int:id>/', views.delete_order_api, name='order-delete'),

    path('order-products/', views.get_order_product_api, name="order-products"),
    path('order-products/<int:id>/', views.get_order_product_api, name="one-order-product"),
    path('order-products/create/', views.add_order_product_api, name='create-order-product'),
    path('order-products/update/<int:id>/', views.update_order_product_api, name='order-product-update'),
    path('order-products/delete/<int:id>/', views.delete_order_product_api, name='order-product-delete'),
]

