from django.urls import path,include
from .views import home, somos, galeria, Unetenos,cliente, crear_cli, modificar_cli, delete_cli,mostrarproductos,forms_productos,form_mod_productos,form_del_productos

urlpatterns = [
    path('', home,name='home'),
    path('somos/', somos,name='somos'),
    path('galeria/', galeria,name='galeria'),
    path('Unetenos/', Unetenos,name='Unetenos'),
    path('cliente/',cliente, name='cliente'),
    path('crear_cli/', crear_cli, name='crear_cli'),
    path('modificar_cli/<id>', modificar_cli, name='modificar_cli'),
    path('delete_cli/<id>',delete_cli, name='delete_cli'),
    path('mostrarproductos/',mostrarproductos,name="mostrarproductos"),
    path('forms_productos/',forms_productos,name="forms_productos"),
    path('form_mod_productos/<id>',form_mod_productos,name="form_mod_productos"),
    path('form_del_productos/<id>',form_del_productos,name="form_del_productos"),
   


]