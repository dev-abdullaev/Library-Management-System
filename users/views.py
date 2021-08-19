from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.views.generic import CreateView

from .forms import CustomUserCreationForm, LoginForm
from .models import User


class SignUpCreateView(CreateView):
    model = User
    template_name = "registration/signup.html"
    form_class = CustomUserCreationForm
    success_url = reverse_lazy("login")


def custom_user_login(request):

    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
        form = LoginForm(request.POST)
        if form.is_valid():
            user = form.save()

        try:

            if request.user.is_superuser:
                user = authenticate(username=username, password=password)
                login(request, user)
                return redirect("admin_page")
            else:
                user = authenticate(username=username, password=password)
                login(request, user)
                return redirect("home")
        except AttributeError:
            return redirect("login")
    else:
        form = LoginForm()

    return render(request, "registration/login.html", {"form": form})


def custom_user_logout(request):
    if request.user.is_authenticated:
        logout(request)
        return redirect("login")
