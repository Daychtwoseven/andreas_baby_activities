from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from backend.decorators import login_required


@login_required
def index_page(request):
    try:
        return render(request, 'frontend/index.html')
    except Exception as e:
        print(e)


def login_page(request):
    try:
        if request.method == "POST":
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                # User is authenticated, log them in
                login(request, user)
                messages.success(request, 'Successfully logged in.')
                return redirect('backend-index-page')  # Replace 'home' with the name of your homepage URL pattern
            else:
                messages.error(request, 'Incorrect Username or Password.')
        return render(request, 'frontend/login.html')
    except Exception as e:
        print(e)


@login_required
def logout_page(request):
    logout(request)
    return redirect('frontend-login-page')
