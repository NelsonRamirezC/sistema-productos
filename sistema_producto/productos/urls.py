from django.urls import path
from . import views

urlpatterns = [
    path('', views.productos, name="productos"),
    path('add/', views.add_productos, name="add_productos"),
    path('add/modelform', views.add_producto_modelform, name="add_producto_modelform"),
]