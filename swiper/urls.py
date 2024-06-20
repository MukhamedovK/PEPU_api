from django.urls import path

from . import views


urlpatterns = [
    path('showcase-swiper/', views.get_showcase_swiper_api, name="main-swiper-images"),
    path('showcase-swiper/<int:id>/', views.get_showcase_swiper_api, name="main-swiper-images"),
    path('showcase-swiper/create/', views.add_showcase_swiper_api, name='create-showcase-swiper'),
    path('showcase-swiper/update/<int:id>/', views.update_showcase_swiper_api, name='showcase-swiper-update'),
    path('showcase-swiper/delete/<int:id>/', views.delete_showcase_swiper_api, name='showcase-swiper-delete'),
    
    path('showcase-sub-swiper/', views.get_showcase_sub_swiper_api, name="showcase_sub_swiper-images"),
    path('showcase-sub-swiper/<int:id>/', views.get_showcase_sub_swiper_api, name="showcase_sub_swiper-image"),
    path('showcase-sub-swiper/create/', views.add_showcase_sub_swiper_api, name='create-showcase_sub_swiper'),
    path('showcase-sub-swiper/update/<int:id>/', views.update_showcase_sub_swiper_api, name='showcase_sub_swiper-update'),
    path('showcase-sub-swiper/delete/<int:id>/', views.delete_showcase_sub_swiper_api, name='showcase_sub_swiper-delete'),

    path('clothes-swiper/', views.get_clothes_swiper_api, name="clothes-swiper-images"),
    path('clothes-swiper/<int:id>/', views.get_clothes_swiper_api, name="clothes-swiper-images"),
    path('clothes-swiper/create/', views.add_clothes_swiper_api, name='create-clothes-swiper'),
    path('clothes-swiper/update/<int:id>/', views.update_clothes_swiper_api, name='clothes-swiper-update'),
    path('clothes-swiper/delete/<int:id>/', views.delete_clothes_swiper_api, name='clothes-swiper-delete'),
]

