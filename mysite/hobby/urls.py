from django.urls import path
from . import views

urlpatterns = [
	path('', views.index),
	path('hobby.html', views.index),
]
