from django.contrib import admin
from django.urls import path
from . views import index_page, persons_page

urlpatterns = [
    path('', index_page, name='backend-index-page'),

    path('persons/', persons_page, name='backend-persons-page'),
    path('persons/<slug:action>/', persons_page, name='backend-persons-page'),
    path('persons/<slug:action>/<slug:pk>/', persons_page, name='backend-persons-page'),
]
