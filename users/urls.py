from django.urls import path

from .views import SignUpCreateView, custom_user_login

urlpatterns = [
    path("signup/", SignUpCreateView.as_view(), name="signup"),
    path("login/", custom_user_login, name="login"),
]
