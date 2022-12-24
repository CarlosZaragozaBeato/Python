
from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path('admin/', admin.site.urls),
    path('one/', include('one_to_one.urls')),
    path('many/', include('many_to_one.urls')),
    path('many2/', include('many_to_many.urls'))
]
