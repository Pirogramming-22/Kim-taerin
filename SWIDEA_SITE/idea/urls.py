from django.urls import path,re_path
from . import views

urlpatterns = [
    path('', views.idea_list, name='idea_list'),
    path('register/', views.idea_register, name='idea_register'),
    path('<int:pk>/', views.idea_detail, name='idea_detail'),
    path('<int:pk>/update/', views.idea_update, name='idea_update'),
    path('<int:pk>/delete/', views.idea_delete, name='idea_delete'),
    path('<int:pk>/toggle_like/', views.toggle_like, name='toggle_like'),  # 찜하기 토글
    re_path(r'^(?P<pk>[0-9]+)/change_interest/(?P<delta>-?\d+)/$', views.change_interest, name='change_interest'),  # 음수 허용
]