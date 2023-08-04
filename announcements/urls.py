#from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('mkannouncements/', views.mkannouncements,name="mkannouncements"),
    path('display/',views.display,name="display"),
    path('view_announcements/',views.view_announcements,name="view_announcements")
]
