from django.contrib import admin
from . import views
from django.urls import path

urlpatterns = [
    path('',views.contacts,name='contacts'),
    path('submitQuery',views.submitQuery,name='submitQuery')
]
