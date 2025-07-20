from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages


def home_view(request):
    # Render the home page
    return render(request, "Index/index.html", {})


def user_logout_view(request):
    # Log the user out and show a success message
    logout(request)
    messages.success(request, "You have successfully logged out!")
    return redirect("home_page")


def user_signup_view(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            # Create and log in the user
            user = form.save()
            login(request, user)
            messages.success(request, "You have successfully signed up and logged in!")
            return redirect("home_page")
        else:
            # Display an error if form is invalid
            messages.error(request, "The fields are not valid. Please check and try again.")
    else:
        # Display empty signup form
        form = UserCreationForm()

    return render(request, "registration/signup.html", {'form': form})


def user_login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            # Authenticate and log in the user
            user = form.get_user()
            login(request, user)
            messages.success(request, f"Welcome back, {user.username}!")
            return redirect("home_page")
        else:
            # Invalid login credentials
            messages.error(request, "Invalid username or password.")
    else:
        # Display empty login form
        form = AuthenticationForm()

    return render(request, "registration/login.html", {'form': form})
