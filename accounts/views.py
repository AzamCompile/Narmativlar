from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from accounts.forms import LoginForm


def register(request):
    form = UserCreationForm()

    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")

    return render(request, "registration/register.html", {"form": form})


def login_view(request):
    form = LoginForm()

    if request.method == "POST":
        form = LoginForm(request.POST)

        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]

            user = authenticate(request, username=username, password=password)

            if user:
                login(request, user)
                return redirect("student-list")
            else:
                form.add_error(None, "Username yoki password noto‘g‘ri")

    return render(request, "accounts/login.html", {"form": form})


def logout_view(request):
    logout(request)
    return redirect('login')
