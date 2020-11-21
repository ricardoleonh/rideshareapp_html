from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),
    path('registration', views.registration),
    path('log_in', views.log_in),
    path('dashboard', views.dashboard),
    path('loggedin', views.loggedin)

]