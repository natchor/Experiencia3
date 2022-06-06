from django.urls import path
from .views import home, somos, galeria, Unetenos

urlpatterns = [
    path('', home,name='home'),
    path('somos/', somos,name='somos'),
    path('galeria/', galeria,name='galeria'),
    path('Unetenos/', Unetenos,name='Unetenos'),
]