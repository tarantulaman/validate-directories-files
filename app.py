# Importamos la libreria de sistema operativo
# para validar el Path existente
import os



# Validamos si existe dentro del directorio un archivo, dentro del directorio
# actual que nos encontremos y lo almacenamos en una variable

# os.getcwd() = permite obtener la ruta del directorio actual en donde nos encontramos
# new_folder = nombre del directorio que vamos a buscar dentro del dierctorio actual
# file.txt = nombre del archivo que vamos a buscar

#var = os.path.exists(os.path.join(os.getcwd(), 'new_folder', 'file.txt'))






# Validamos si existe dentro de un directorio culaquiera un archivo

# /home/fersilent/Documentos = ruta del directorio donde vamos a buscar el archivo
# new_folder = nombre del directorio que vamos a buscar dentro del dierctorio actual
# programming-directories.db = nombre del archivo que vamos a buscar

var = os.path.exists(os.path.join("/home/fersilent/Documentos", 'programming-directories.db'))







# Al imprimir la variable, si existe el directorio y el archivo imprimira True de lo contrario False
print(var)
