from django.urls import path
from . import views

from . import views 
urlpatterns = [
    path('create', views.create, name="create")
]
