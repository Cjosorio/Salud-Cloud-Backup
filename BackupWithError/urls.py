from django.urls import path, include
from rest_framework import routers
from .views import BackupWithErrorListView
from BackupWithError import views
from django.contrib import admin


urlpatterns = [
    path('backups-with-errors/', BackupWithErrorListView.as_view(), name='backups-with-errors'),
]