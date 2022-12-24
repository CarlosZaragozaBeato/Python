
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name="index"),
    path('profile/',views.profile, name="profile"),
    path('galery', views.galery, name="galery")

]
