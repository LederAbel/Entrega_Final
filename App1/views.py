from django.shortcuts import render
from django.http import HttpResponse
import datetime, random 
from App1.models import *
from App1.forms import *
def inicio(request):
    
    return render(request, "App1/inicio.html")

def nuevo_cliente(request):
    
    client = Cliente(nombre = "Abel",apellido ="Leder", direccion = "Entre Rios 1191",localidad="Bella Vista",provincia="Buenos Aires",pais="Argentina")
    
    client.save()
    
    return render(request, "App1/nuevo_cliente.html")
    
def cliente_formulario(request):
    
    if request.method == "POST":
        
        formulario1 = Cliente_Formulario(request.POST)
        
        if formulario1.is_valid():
            
            info = formulario1.cleaned_data
            
            cliente = Cliente(nombre=info["nombre"],apellido=info["apellido"],email=info["email"],direccion=info["direccion"],localidad=info["localidad"],provincia=info["provincia"],pais=info["pais"])            
            
            cliente.save()
            return render(request,"App1/inicio.html")
    else:
    
        formulario1= Cliente_Formulario()
    
    return render(request,"App1/cliente_formulario.html",{"form1":formulario1})

def reparacion(request):
     
    if request.method == "POST":
        
        formula1 = Reparacion_Formulario(request.POST)
        
        if formula1.is_valid():
            
            info = formula1.cleaned_data
            
            reparacion = PedalReparar(nombre=info["modelo"],efecto=info["efecto"],fabricante=info["fabricante"],volts=info["volts"],origen=info["origen"],cliente=info["cliente"],falla=info["falla"],envio=info["envio"],)            
            reparacion.save()
            return render(request,"App1/inicio.html")
    else:
    
         formula1= Reparacion_Formulario()
    
     
         return render (request,"App1/reparacion_formulario.html",{"form2":formula1})


# CRUD StockPropio

def leer_stockpropio(request):
    
    pedal = StockPropio.objects.all()
    
    contexto = {"modelopropio": pedal}
    
    return render (request,"App1/pedalespropios.html", contexto)

def crear_stockpropio(request): 
    if request.method == "POST":
        
        formula1 = StockPropio_Formulario(request.POST)
        
        if formula1.is_valid():
            
            info = formula1.cleaned_data
            
            modelopropio = StockPropio(modelo=info["modelo"],efecto=info["efecto"],unidades=info["unidades"],descripcion=info["descripcion"],precio=info["precio"])            
            modelopropio.save()
            return render(request,"App1/inicio.html")
    else:
        
         formula1= StockPropio_Formulario()
    
     
         return render (request,"App1/nuevo_stock_propio.html",{"form1":formula1})
    
def eliminar_stockpropio(request,modelopropio):
    
    modelo= StockPropio.objects.get(modelo=modelopropio)
    modelo.delete()
    
    modelo=StockPropio.objects.all()
    contexto={"nombre":modelo}
    
    return render(request,"App1/pedalespropios.html",contexto)
    
def editar_stockpropio(request, modelopropio):
    
    pedalpropio= StockPropio.objects.get(modelo=modelopropio)
    
    if request.method == "POST":
        
        formula1 = StockPropio_Formulario(request.POST)
        
        if formula1.is_valid():
            
            info = formula1.cleaned_data
            
            pedalpropio.modelo= info["modelo"]
            pedalpropio.efecto= info["efecto"]
            pedalpropio.unidades= info["unidades"]
            pedalpropio.descripcion= info["descripcion"]
            pedalpropio.precio= info["precio"]
            pedalpropio.save()
            return render(request,"App1/inicio.html")
    else:
        
         formula1= StockPropio_Formulario(initial={"modelo":pedalpropio.modelo, "efecto":pedalpropio.efecto,
            "unidades":pedalpropio.unidades,"descricion":pedalpropio.descripcion,"precio":pedalpropio.precio})
    
     
         return render (request,"App1/editar_stock_propio.html",{"form1":formula1}, {"modelo": modelopropio})
        
# Esto lo voy a borrar
def mostrar_resultados(request):
    
    if request.GET["modelo"]:
        
        modelo = request.GET["modelo"]
        
        modelos= StockPropio.objects.filter(modelo__icontains=modelo)
        unidades = StockPropio.objects.filter(modelo__icontains=modelo)
        
        return render (request, "App1/resultadostock.html",{"modelos":modelos ,"unidades":unidades})
    else:
        respuesta = "No enviaste datos."
    
    return HttpResponse(respuesta)