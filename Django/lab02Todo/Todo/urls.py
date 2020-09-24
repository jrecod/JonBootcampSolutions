from django.urls import path
from . import views

app_name = 'Todo'
urlpatterns = [
    path('index/', views.index, name='index')
]