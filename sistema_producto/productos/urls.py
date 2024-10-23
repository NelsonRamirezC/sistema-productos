from django.urls import path
from . import views

urlpatterns = [
    path('', views.productos, name="productos"),
    path('add/', views.add_productos, name="add_productos"),
    path('add/modelform', views.add_producto_modelform, name="add_producto_modelform"),
    path('productos_vip/', views.productos_vip, name="productos_vip"),
    path('productos_destacados/', views.productos_destacados, name="productos_destacados"),
]