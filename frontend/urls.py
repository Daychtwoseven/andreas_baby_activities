from django.contrib import admin
from django.urls import path
from . views import login_page, logout_page
from backend.views import index_page

urlpatterns = [
    path('', index_page, name='frontend-index-page'),
    path('login/', login_page, name='frontend-login-page'),
    path('logout/', logout_page, name='frontend-logout-page')
]
