from django.urls import path
from . import views

urlpatterns = [
    path('api/', views.get_info, name='get_info'),
    path('', views.root_view, name='root_view'),  # Handle the root URL
]