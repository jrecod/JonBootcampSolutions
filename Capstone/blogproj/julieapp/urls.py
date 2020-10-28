from django.urls import path
from . import views

app_name = 'julieapp'
urlpatterns = [
    path('login/', views.login_request, name='login'),
    path('logout/', views.logout_request, name='logout'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('create/', views.create_post, name='create'),
    path('edit/<str:post_id>/', views.edit_post, name='edit'),
    path('delete/<int:post_id>/', views.delete_post, name='delete'),
]