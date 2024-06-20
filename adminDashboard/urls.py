from django.urls import path

from . import views


urlpatterns = [
    path('login/', views.login_profile_api, name='login-user'),
    path('registration/', views.add_profile_api, name='create-profile'),

    path('profile/', views.get_profile_api, name="profiles"),
    path('profile/<int:id>/', views.get_profile_api, name="one-profile"),
    path('profile/update/<int:id>/', views.update_profile_api, name='profile-update'),
    path('profile/delete/<int:id>/', views.delete_profile_api, name='profile-delete'),

    path('branch/', views.get_branch_api, name="branches"),
    path('branch/<int:id>/', views.get_branch_api, name="one-branch"),
    path('branch/create/', views.add_branch_api, name='create-branch'),
    path('branch/update/<int:id>/', views.update_branch_api, name='branch-update'),
    path('branch/delete/<int:id>/', views.delete_branch_api, name='branch-delete'),
]

