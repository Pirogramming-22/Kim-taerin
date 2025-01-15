from django.urls import path
from . import views

urlpatterns = [
    path('', views.idea_list, name='idea_list'),
    path('register/', views.idea_register, name='idea_register'),
    path('<int:pk>/', views.idea_detail, name='idea_detail'),
    path('<int:pk>/update/', views.idea_update, name='idea_update'),
    path('<int:pk>/delete/', views.idea_delete, name='idea_delete'),
]