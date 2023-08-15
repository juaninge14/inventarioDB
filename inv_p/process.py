# Descarga, Procesamiento y Actualizacion 
# de la BD cuando el archivo CSV es descargado

import csv
from .models import Cliente, Sucursal, Producto, Inventario     # Importamos los modelos


# Procesamiento y actualización de la base de datos
with open("inventario.csv", "r") as csv_file:
    csv_reader = csv.DictReader(csv_file)
    for row in csv_reader:
        # Obtenemos los datos del archivo CSV
        fecha_inventario = row["FechaInventario"]
        gln_cliente = row["GLN_Cliente"]
        gln_sucursal = row["GLN_sucursal"]
        gtin_producto = row["Gtin_Producto"]
        inventario_final = int(row["Inventario_Final"])
        precio_unidad = float(row["PrecioUnidad"])

        # Buscamos o creamos los objetos relacionados en la BD
        cliente, created = Cliente.objects.get_or_create(GLN_Cliente=gln_cliente)
        sucursal, created = Sucursal.objects.get_or_create(GLN_sucursal=gln_sucursal, cliente=cliente)
        producto, created = Producto.objects.get_or_create(Gtin_Producto=gtin_producto)

        # Creamos o actualizamos el registro de inventario
        inventario, created = Inventario.objects.get_or_create(
            FechaInventario=fecha_inventario,
            sucursal=sucursal,
            producto=producto,
            defaults={
                "Inventario_Final": inventario_final,
                "PrecioUnidad": precio_unidad
            }
        )
        if not created:
            # Actualizamos los valores en caso de existir
            inventario.Inventario_Final = inventario_final
            inventario.PrecioUnidad = precio_unidad
            inventario.save()