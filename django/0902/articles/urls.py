from django.urls import path
from . import views

app_name = 'articles'
urlpatterns = [
    path('', views.index, name='index'),
    path('new/', views.new, name='new'),
    path('create/', views.create, name ='create'),
    path('<int:pk>/', views.detail, name='detail'), # http://127.0.0.1:8000/1 1번 게시글 상세, variable routing
    path('<int:pk>/delete/', views.delete, name="delete"),
    path('<int:pk>/edit/', views.edit, name="edit"),
    path('<int:pk/update/', views.update, name="update"),
] 
