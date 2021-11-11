from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('',views.registerView,name='register'),
    path('home/',views.homeView,name='home'),
    path('login/',auth_views.LoginView.as_view(template_name='User/login.html'),name='login'),
    path('logout/',auth_views.LogoutView.as_view(template_name='User/logout.html'),name='logout'),
]
