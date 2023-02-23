from django.urls import path
from App1.views import *
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    
    path("",inicio, name="Inicio"),
    path("nvo_cliente/", nuevo_cliente, name="NuevoCliente"),
    path("cliente_formulario/",cliente_formulario, name="FormularioCliente"),
    path("reparacion_formulario/", reparacion, name="FormularioReparacion"),
    path("resultados_stock/", mostrar_resultados ,name="Resultados"),
    
    #CRUD StockPropio
    
    path("leer_stockpropio/", leer_stockpropio, name="StockPropio"),
    path("crear_stockpropio/", crear_stockpropio, name="NuevoStockPropio"),
    path("eliminar_stockpropio/<modelopropio>", eliminar_stockpropio, name="Eliminar_stockpropio"),
    path("editar_stockpropio/<modelopropio>", editar_stockpropio, name="Editar_stockpropio"),
]

#Imagen Soyus

urlpatterns += staticfiles_urlpatterns()