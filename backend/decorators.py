from functools import wraps
from django.shortcuts import redirect

def login_required(view_func):
    """
    Custom login_required decorator for function-based views.
    Redirects to the login page if the user is not authenticated.
    """
    @wraps(view_func)
    def wrapped_view(request, *args, **kwargs):
        if not request.user.is_authenticated:
            # Redirect to login page or any other page of your choice
            return redirect('frontend-login-page')  # Replace 'login' with your actual login URL
        return view_func(request, *args, **kwargs)
    return wrapped_view