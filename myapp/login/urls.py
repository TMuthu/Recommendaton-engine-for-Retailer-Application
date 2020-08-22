from django.urls import path
from . import views
from django.contrib import admin

urlpatterns = [
    path('signin', views.signin, name='signin'),
    path('signup', views.signup, name='signup'),
    path('result', views.result, name='result'),
]
