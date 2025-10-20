from django.db import models

# Create your models here.
class Automovil(models.Model):
    marca = models.CharField(max_length=50)
    modelo = models.CharField(max_length=50)
    anio = models.IntegerField()
    precio = models.DecimalField(max_digits=10, decimal_places=2)
    disponible = models.BooleanField(default=True)
    descripcion = models.TextField(blank=True, null=True)
    imagen = models.ImageField(upload_to='autos/', blank=True, null=True)

    def __str__(self):
        return f"{self.marca} {self.modelo} ({self.anio})"
