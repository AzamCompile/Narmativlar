from django.contrib.auth import authenticate, login, logout
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from accounts.forms import LoginForm, RegisterForm


def register(request):
    form = RegisterForm()

    if request.method == "POST":
        form = RegisterForm(request.POST)

        if form.is_valid():
            user = form.save()

            send_mail(
                subject="Ro‘yxatdan o‘tish muvaffaqiyatli",
                message="Siz Django kursga muvaffaqiyatli ro‘yxatdan o‘tdingiz.",
                from_email=None,
                recipient_list=[user.email],
                fail_silently=False,
            )

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
    return redirect("login")
