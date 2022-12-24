from django.db import models

# Create your models here.


class Pais(models.Model):
    name = models.CharField(max_length=20, null = False)
    country_code = models.CharField(max_length=30)
    
    def __str__(self):
        return self.name
    

class Localizacion(models.Model):
    name = models.CharField(max_length=30, null = False)
    country = models.ForeignKey(Pais, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Salario(models.Model):
    amount = models.IntegerField(null = False, blank=False)
    extra_dec = models.BooleanField(default=False)
    extra_jun = models.BooleanField(default=False)
    
    def __str__(self):
        return self.amount


class Trabajo(models.Model):
    title = models.CharField(max_length=20, null=False, blank=False)
    description = models.CharField(max_length=30)
    salary = models.ForeignKey(Salario, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
    
    
class Lugar(models.Model):
    name = models.CharField(max_length=20, null=False, blank=False)
    address = models.CharField(max_length=30, null = False)
    zipcode = models.CharField(max_length=10)
    location = models.ForeignKey(Localizacion, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Empleado(models.Model):
    id_number = models.CharField(max_length=10, null=False, blank=False)
    name = models.CharField(max_length=25, null=False, blank=False)
    last_name = models.CharField(max_length=30 )
    email = models.EmailField(max_length=50, null=False, blank=False)
    address = models.CharField(max_length=50)
    job = models.ForeignKey(Trabajo, on_delete= models.CASCADE)
    place = models.ForeignKey(Lugar, on_delete=models.CASCADE)
    
    def __str__(self):
        return self.name
    
