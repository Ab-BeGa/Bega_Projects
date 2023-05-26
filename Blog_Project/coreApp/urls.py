from django.urls import path
from . import views

urlpatterns = [
    path('', views.homePage, name='homePage'),
    path('post/view/<int:pk>/', views.postDetail, name='postDetail'),
    path('post/add/', views.addPost, name='addPost'),
    path('post/delete/<int:pk>/', views.deletePost, name='deletePost'),
    path('post/edit/<int:pk>/', views.editPost, name='editPost'),
    path('user/favorite_posts/', views.favorite_posts, name='favorite_posts'),
    path('user/add_to_favorite/<int:pk>/', views.add_to_favorite, name='add_to_favorite'),
    path('user/remove_from_favorite/<int:pk>/', views.remove_from_favorite, name='remove_from_favorite'),
    path('user/sign-up/', views.signUp, name='signUp'),
    path('user/login/', views.loginUser, name='loginUser'),
    path('user/logout/', views.logoutUser, name='logoutUser'),
]