from django.urls import path
from . import views


urlpatterns = [
  path('book/', views.index, name = 'index')
]