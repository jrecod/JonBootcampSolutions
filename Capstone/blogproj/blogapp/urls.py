from django.urls import path
from . import views

app_name = 'blogapp'
urlpatterns = [
    path('', views.home, name='home'),
    path('category/<str:path_name>/', views.category, name='category'),
    path('post/<int:post_id>/', views.blog_post, name='post'),
    path('about/', views.about_me, name='about')
]