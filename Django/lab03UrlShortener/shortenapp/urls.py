from django.urls import path
from . import views

app_name='shortenapp'
urlpatterns = [
    path('', views.index, name='index'),
    path('save/', views.save, name='save'),
    path('redirect/<str:code>/', views.url_redirector, name='url_redirector'),
]