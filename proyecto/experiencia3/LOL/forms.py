from django import forms
from django.forms import ModelForm
from django.forms import widgets
from django.forms.models import ModelChoiceField
from django.forms.widgets import Widget
from .models import Cliente, Productos, Comuna


class clienteForm(forms.ModelForm):
    class Meta:
        model= Cliente
        fields = ['rut', 'nombre', 'apellidos', 'correo', 'password', 'fono', 'direccion', 'comuna']
        labels ={
            'rut' : 'Rut',
            'nombre' : 'Nombre',
            'apellidos' : 'Apellidos',
            'correo' : 'Correo',
            'password' : 'Password',
            'fono' : 'Fono',
            'direccion' : 'Direccion',
            'comuna' : 'Comuna' 
        }
        widgets={
            'rut' : forms.TextInput(
                attrs={
                    'class' : 'form-control',
                    'placeholder' : 'ingrese su rut',
                    'id' : 'rut'
                }
            ),
            
            'nombre' : forms.TextInput(
                attrs={
                    'class' : 'form-control',
                    'placeholder' : 'ingrese su nombre',
                    'id' : 'nombre'
                }
            ),
            'apellidos' : forms.TextInput(
                attrs={
                    'class' : 'form-control',
                    'placeholder' : 'ingrese sus apellidos',
                    'id' : 'apellidos'
                }
            ),
            'correo' : forms.TextInput(
                attrs={
                    'class' : 'form-control',
                    'placeholder' : 'ingrese su correo',
                    'id' : 'correo'
                }
            ),
            'password' : forms.TextInput(
                attrs={
                    'class' : 'form-control',
                    'placeholder' : 'ingrese su password',
                    'id' : 'password'
                }
            ),
            'fono' : forms.TextInput(
                attrs={
                    'class' : 'form-control',
                    'placeholder' : 'ingrese su fono',
                    'id' : 'fono'
                }
            ),
            'direccion' : forms.TextInput(
                attrs={
                    'class' : 'form-control',
                    'placeholder' : 'ingrese su direccion',
                    'id' : 'direccion'
                }
            ),
            'comuna': forms.Select(
                attrs={
                    'class': 'form-control',
                    'id': 'comuna',
                }
            )
            
        }
class ProductosForm(forms.ModelForm):
    class Meta:
        model = Productos
        fields = ['idproducto', 'nombre', 'imagen', 'description', 'cantidad', 'precio']
        labels = {
            'idproducto': 'idproducto',
            'nombre': 'nombre',
            'imagen': 'imagen',
            'description': 'description',
            'cantidad': 'cantidad',
            'precio': 'precio',
        }
        widgets = {
            'idproducto': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese el id del producto',
                    'id': 'idproducto'
                }
            ),
            'nombre': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese el nombre del producto',
                    'id': 'nombre'
                }
            ),
            'imagen': forms.FileInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese la imagen del producto',
                    'id': 'imagen'
                }
            ),
            'description': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese la descripcion del producto',
                    'id': 'description'
                }
            ),
            'cantidad': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese la cantidad del producto',
                    'id': 'cantidad'
                }
            ),
            'precio': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese el precio del producto',
                    'id': 'precio'
                }
            )
        }