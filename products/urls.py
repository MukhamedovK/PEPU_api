from django.urls import path

from . import views


urlpatterns = [
    path('products/', views.get_product_api, name="products"),
    path('products/<int:id>/', views.get_product_api, name="one-product"),
    path('products/create/', views.add_product_api, name='create-product'),
    path('products/update/<int:id>/', views.update_product_api, name='product-update'),
    path('products/delete/<int:id>/', views.delete_product_api, name='product-delete'),

    path('categories/', views.get_category_api, name="categories"),
    path('categories/<int:id>/', views.get_category_api, name='one-category'),
    path('categories/create/', views.add_category_api, name='create-category'),
    path('categories/update/<int:id>/', views.update_category_api, name='category-update'),
    path('categories/delete/<int:id>/', views.delete_category_api, name='category-delete'),

    path('sizes/', views.get_size_api, name="sizes"),
    path('sizes/<int:id>/', views.get_size_api, name="one-size"),
    path('sizes/create/', views.add_size_api, name='create-sizes'),
    path('sizes/update/<int:id>/', views.update_size_api, name='sizes-update'),
    path('sizes/delete/<int:id>/', views.delete_size_api, name='sizes-delete'),

    path('product-photo/', views.get_product_photo_api, name="product-photos"),
    path('product-photo/<int:id>/', views.get_product_photo_api, name="one-product-photo"),
    path('product-photo/create/', views.add_product_photo_api, name='create-product-photo'),
    path('product-photo/update/<int:id>/', views.update_product_photo_api, name='product-photo-update'),
    path('product-photo/delete/<int:id>/', views.delete_product_photo_api, name='product-photo-delete'),
]

