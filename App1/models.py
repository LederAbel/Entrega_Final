from django.db import models
import datetime

class Cliente(models.Model):
    
    def __str__(self):
        
        return f"cliente: {self.nombre} {self.apellido}" 
    
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    email = models.EmailField(default="pedal@gmail.com")
    direccion = models.CharField(max_length=80)
    localidad = models.CharField(max_length=50)
    provincia = models.CharField(max_length=50)
    pais = models.CharField(max_length=50)
    
class StockPropio(models.Model):
    
    def __str__(self):
        
        return f"modelo: {self.modelo}---- unidades:{self.unidades}"
    
    modelo = models.CharField(max_length=50)
    efecto = models.CharField(max_length=50)
    unidades = models.CharField(max_length=20)
    descripcion = models.TextField()
    precio = models.CharField(max_length=20)
    
class PedalReparar(models.Model):
    
    def __str__(self):
        return f"Pedal: {self.nombre}---- cliente:{self.cliente}"
        
    nombre = models.CharField(max_length=50) #Nombre del pedal
    efecto = models.CharField(max_length=50) #Tipo de Efecto
    fabricante = models.CharField(max_length=50)
    volts = models.CharField(max_length=20) #alimentacion
    made = models.CharField(max_length=50) #procedencia
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    falla = models.TextField(max_length=500,default="Falla")
    envio = models.CharField(max_length=60)
    fechapedido = models.DateTimeField(blank=False, null=True, auto_now_add=True)
   
class PedalClon(models.Model):
    clon_de = models.CharField(max_length=80)
    mods = models.TextField()
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    envio = models.BooleanField()
    descripcion = models.TextField(max_length=500,default="Descripcion del pedal")
    fechapedido = models.DateTimeField(null=True, auto_now_add=True)

class VentaPropio(models.Model):
    modelo = models.ForeignKey(StockPropio, on_delete=models.CASCADE)
    cantidad = models.IntegerField()
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    envio = models.BooleanField(default=True)
    fechapedido = models.DateTimeField(null=True, auto_now_add=True)



      
      