from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm
from django.shortcuts import redirect, render
from django.utils.translation import gettext as _


def register_view(request):
    """
    Handle user registration.

    Processes POST requests with user registration data using Django's
    built-in UserCreationForm. On successful registration, redirects to login page.
    For GET requests, displays the empty registration form.

    Args:
        request (HttpRequest): HTTP request object.

    Returns:
        HttpResponse: Rendered registration form or redirect to login page.
    """
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("login")
    else:
        form = UserCreationForm()
    return render(request, "accounts/register.html", {"form": form})


def login_view(request):
    """
    Handle user login.

    Processes POST requests with login credentials using Django's
    AuthenticationForm. On successful authentication, logs in the user and redirects
    to the dashboard page. For GET requests, displays the empty login form.

    Args:
        request (HttpRequest): HTTP request object.

    Returns:
        HttpResponse: Rendered login form or redirect to dashboard.
    """
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect("dashboard")
    else:
        form = AuthenticationForm()
    return render(request, "accounts/login.html", {"form": form})


def logout_view(request):
    """
    Log out the current user and redirect to the login page.

    Args:
        request (HttpRequest): HTTP request object.

    Returns:
        HttpResponseRedirect: Redirect response to the login page.
    """
    logout(request)
    return redirect("login")
