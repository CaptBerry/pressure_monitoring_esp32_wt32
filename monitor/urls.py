from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard_view, name='dashboard'),  # главная страница
    path('api/status/', views.api_status, name='api_status'),
]
