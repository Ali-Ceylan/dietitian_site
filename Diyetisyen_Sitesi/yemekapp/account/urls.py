from django.urls import path
from . import views


urlpatterns = [
    path("login", views.login_request, name="login"),
    path("register", views.register_request, name="register"),
    path("logout", views.logout_request, name="logout"),
    path("diyetisyenlogin", views.diyetisyenlogin_request, name="diyetisyenlogin"),
]
"""
from django.urls import path
from .views import register_user, register_doctor

urlpatterns = [
    path('register/user/', register_user, name='register_user'),
    path('register/doctor/', register_doctor, name='register_doctor'),
]
"""