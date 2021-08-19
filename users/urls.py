from django.urls import path

from .views import SignUpCreateView, custom_user_login, custom_user_logout

urlpatterns = [
    path("signup/", SignUpCreateView.as_view(), name="signup"),
    path("login/", custom_user_login, name="login"),
    path("logout/", custom_user_logout, name="logout"),
]
