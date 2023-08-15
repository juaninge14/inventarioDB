# Creamos los modelos de la BD de la siguiente manera 
# Tenemos en cuenta las relaciones de las entidades 

from django.db import models

               
# Modelo Clientes
class Cliente(models.Model):                # Clase cliente
    GLN_Cliente = models.CharField(max_length=50, unique=True)      # Atributos
    
    def __str__(self):                      # Metodo
        return self.GLN_Cliente


# Modelo Sucursal             
class Sucursal(models.Model):               # Clase sucursal
    GLN_sucursal = models.CharField(max_length=50, unique=True)     
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)     # Atributos en cascada para las relaciones
    
    def __str__(self):                      # Metodo
        return self.GLN_sucursal


# Modelo Producto
class Producto(models.Model):               # Clase producto
    Gtin_Producto = models.CharField(max_length=50, unique=True)    # Atributos
    
    def __str__(self):                      # Metodo
        return self.Gtin_Producto


# Modelo inventario
class Inventario(models.Model):             # Clase inventario
    FechaInventario = models.DateField()
    sucursal = models.ForeignKey(Sucursal, on_delete=models.CASCADE)
    producto = models.ForeignKey(Producto, on_delete=models.CASCADE)    # Atributos en cascada para las relaciones
    Inventario_Final = models.IntegerField()
    PrecioUnidad = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):                      # Metodo
        return f"Inventario {self.producto} en {self.sucursal} el {self.FechaInventario}"
