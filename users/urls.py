from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.loginUser, name='login'),
    path('logout/', views.logoutUser, name='logout'),
    path('register/', views.registerUser, name='register'),
    
    
    path('', views.profile, name='profile'),
    path('profiles/<str:pk>', views.userProfile, name='user-profile'),
]