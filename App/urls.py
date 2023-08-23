from django.urls import path
from .views import Cliente, Empleado, Compra


urlpatterns = [
    path("Cliente/", Cliente, name="cliente"),
    path("Empleado/", Empleado, name= "empleado"),
    path("Compra/", Compra, name= "compra"),
]

