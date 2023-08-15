# Creamos un archio con la configuracion especifica del blob para azure

from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient

# Configuramos las credenciales de la cuenta de almacenamiento de Azure
account_name = "storageinv"
account_key = "qJuBPnZyayaD/0+uHkX1bdCc8vd/iAc9OcRBTV8zkJ9Yk9A8dklcc1VQWUay50ubxVaP+mITTkxw+AStCrFdQw=="
container_name = "inventario"
blob_name = "inventario.csv"
local_file_path = "J:\Documentos\Profesion\Trabajos\Desarrollos software\Prueba_Python Juan Camilo Velasquez\inv_p"  # Ruta al archivo en tu sistema local

# Creamos el cliente de servicio Blob
blob_service_client = BlobServiceClient(account_url=f"https://{account_name}.blob.core.windows.net", credential=account_key)

# Obtenemos una referencia al contenedor creado
container_client = blob_service_client.get_container_client(container_name)
container_client.create_container()

# Subimos el archivo al blob storage
blob_client = blob_service_client.get_blob_client(container=container_name, blob=blob_name)
with open(local_file_path, "rb") as data:
    blob_client.upload_blob(data, overwrite=True)

print(f"Archivo '{blob_name}' cargado exitosamente en el contenedor '{container_name}'.")





# Verificamos si el blob existe en la cuenta azure
blob_exists = blob_client.exists()

if blob_exists:
    print(f"El archivo '{blob_name}' existe en el contenedor '{container_name}'.")
else:
    print(f"El archivo '{blob_name}' no existe en el contenedor '{container_name}'.")
