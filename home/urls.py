from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('exit/', views.exit, name="exit"),
    path('signup/', views.signup, name="signup"),
]
