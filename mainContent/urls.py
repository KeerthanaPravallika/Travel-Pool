from django.contrib import admin
from . import views
from django.urls import path

urlpatterns = [
    path('',views.home,name='home'),
    path('pools',views.pools,name='pools'),
    path('searching',views.searching,name='searching'),
    path('form', views.poolsForm,name='poolsForm'),
    path('addToPool/<value>',views.addToPool,name='addToPool'),
    path('addDetails',views.addDetails,name='addDetails'),
    path('viewMembers/<value>',views.viewMembers,name='viewMembers'),
    path('chat',views.chat,name='chat')
]