from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name = 'index'),
    path("details/", views.book_details_2, name = 'book_details'),
    path("members/", views.members, name = 'members')
]
