from django.urls import path, include
from django.contrib.auth import views as auth_views
from authentication import views

urlpatterns = [
    # login view from auth_views with custom login template
    path('login/', auth_views.LoginView.as_view(template_name='authentication/login.html',
                                                # True means that if user is already logged in, it will redirect to homepage
                                                redirect_authenticated_user=True), name='login'),

    # logout view from auth_view
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),

    # path for homepage where successfull login will redirect
    path('', views.homepage, name='homepage'),




]