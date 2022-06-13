from django.shortcuts import render, redirect
from django.views.decorators import csrf
from .models import Cliente , Productos, Comuna
from .forms import clienteForm , ProductosForm
# Create your views here.

def home(request):

    return render(request, 'apps/home.html')

def somos(request):

    return render(request, 'apps/somos.html')

def galeria(request):

    return render(request, 'apps/galeria.html')

def Unetenos(request):

    c

def cliente(request):
    clientes = Cliente.objects.all()
    
    datos1={
        'clientes' : clientes
    }

    return render(request, 'apps/cliente.html',datos1)

def crear_cli(request):
    if request.method=='POST':
        cliente_form = clienteForm(request.POST)
        if cliente_form.is_valid():
            cliente_form.save()
            return redirect ('apps/cliente')
    else:
        cliente_form = clienteForm()
    return render(request, 'apps/crear_cli.html', {'cliente_form': cliente_form})

def modificar_cli(request, id):
    cliente = Cliente.objects.get(rut=id)
    datos2 = {
        'form': clienteForm(instance = cliente)
    }
    if request.method=='POST':
        formulario = clienteForm(data=request.POST, instance = cliente)
        if formulario.is_valid():
            formulario.save()
            datos2['mensaje'] = "modificado correctamente"
            return redirect ('apps/cliente')
        
    return render(request, 'apps/modificar_cli.html', datos2)

def delete_cli(request,id):
    cliente = Cliente.objects.get(rut=id)
    cliente.delete()
    return redirect('apps/cliente')

def mostrarproductos(request):
    productos = Productos.objects.all()
    datos={
        'productos' : productos
    }
    return render(request,'apps/mostrarproductos.html',datos)

def forms_productos(request):
    if request.method=='POST':
        productos_form = ProductosForm(request.POST)
        if productos_form.is_valid():
            productos_form.save()
            return redirect('apps/mostrarproductos')
    else:
        productos_form = ProductosForm()
        return render(request,'apps/forms_productos.html',{'productos_form' : productos_form})

def form_mod_productos(request, id):
    producto = Productos.objects.get(idproducto=id)
    datos3 = {
        'form': ProductosForm(instance = producto)
    }
    if request.method=='POST':
        formulario = ProductosForm(data=request.POST, instance = producto)
        if formulario.is_valid():
            formulario.save()
            datos3['mensaje'] = "modificado correctamente"
            return redirect ('apps/mostrarproductos')
        
    return render(request, 'apps/mostrarproductos.html', datos3)

def form_del_productos(request,id):
    productos = CProductos.objects.get(idproducto=id)
    productos.delete()
    return redirect('apps/mostrarproductos')





