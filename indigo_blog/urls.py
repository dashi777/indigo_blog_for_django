from django.urls import path
from . import views

app_name = 'indigo_blog'
urlpatterns = [
    path('',views.index,name = 'index'),
    path('posts/',views.blog_index,name='blog_index'),
    path('posts/<int:pk>/', views.detail, name='detail'),
    path('projects/',views.project_index,name='project_index'),
    path('project/<int:pk>/', views.project_post, name='project_post'),
]