from django.urls import path
from . import views

app_name = 'blogapp'
urlpatterns = [
    path('', views.home, name='home'),
    path('category/<str:path_name>/', views.category, name='category'),
]