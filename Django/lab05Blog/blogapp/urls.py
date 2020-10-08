from django.urls import path
from django.conf import settings
from . import views
from django.conf.urls.static import static

app_name = 'blogapp'
urlpatterns = [
    path('', views.index, name='index'),
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('profile/', views.profile, name='profile'),
    path('create/', views.create, name='create'),
    path('edit/<int:post_id>/', views.edit, name='edit'),
    path('posts', views.posts, name='posts'),
    path('details/<int:post_id>', views.details, name='details')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)