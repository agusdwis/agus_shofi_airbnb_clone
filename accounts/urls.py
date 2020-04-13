from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views as accounts_views

urlpatterns = [
    path('signup/', accounts_views.signup, name='signup'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('login/', auth_views.LoginView.as_view(template_name='accounts/login.html'), name='login'),

]

app_name = 'accounts'
