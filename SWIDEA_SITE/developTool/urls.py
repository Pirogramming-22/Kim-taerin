from django.urls import path
from . import views

urlpatterns = [
    path('', views.developtool_list, name='developtool_list'),
    path('register/', views.developtool_register, name='developtool_register'),
    path('<int:pk>/', views.developtool_detail, name='developtool_detail'),
    path('<int:pk>/update/', views.developtool_update, name='developtool_update'),
    path('<int:pk>/delete/', views.developtool_delete, name='developtool_delete'),
]
