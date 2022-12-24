from django.contrib import admin
from django.urls import path

from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('saludo/',view= views.saludo, name="saludo"),
    path('despedida/', view = views.despedida, name="despedida"),
    path('adulto/<int:edad>',view = views.adulto,name="adulto")
]
