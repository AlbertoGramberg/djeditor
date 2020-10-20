"""
"""
from django.urls import path
from . import views

app_name = "blog_app"

urlpatterns = [
    path('', views.BlogListView.as_view(), name="index"),
    path('blog/<pk>/', views.BlogDetailView.as_view(), name="detalle"),
    path('blog-add/', views.BlogCreateView.as_view(), name="add"),
]
