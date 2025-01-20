import json
import tempfile
from tabulate import tabulate
from formula.PARA_TODO import *


libros = openJSON("libros")  # Carga la lista de libros desde un archivo JSON
def añadirEle():
        while True:
                opc = input("ingrese s para añadir un nuevo libro y 0 para terminar: ")
                if opc == '0' :
                        break     
                # Mostrar la colección actual
                print(tabulate(libros, headers="keys", tablefmt="grid"))
                titulo = input("Título: ")                     # Solicitar datos al usuario
                autor = input("Autor: ")
                genero = input("Género: ")
                año = input("Año: ")
                descripcion = input("Descripción: ")
                # Crear el nuevo libro como un diccionario
                nuevo_libro = {
                        "titulo": titulo,
                        "autor": autor,
                        "genero": genero,
                        "anio_publicacion": año,
                        "descripcion": descripcion
                        }
                        # Añadir el libro a la colección
                libros.append(nuevo_libro)
                # Retornar el libro añadido
                libroNuevo = añadirEle()                # Llamar a la función para añadir un libro y guardar el resultado en `libroNuevo`
                print(libroNuevo)
                print("Nuevo libro añadido:")           # Mostrar el nuevo libro añadido en formato tabular
                print(tabulate(libroNuevo, headers="keys", tablefmt="grid"))

                with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.json') as archivo_temp:
                # Guardar los datos JSON en el archivo temporal
                        json.dump(libroNuevo, archivo_temp, indent=4)
                print(f"Archivo JSON temporal creado en: {archivo_temp.name}")
                return nuevo_libro 
                


def ver_libros():
        print(tabulate(libros, headers="keys", tablefmt="grid"))



def Libros():
        libros = openJSON("libros")
        tatiana = []
        for diccionario in libros:
                diccionario.pop("descripcion")  
                diccionario.pop("anio_publicacion")
                diccionario.pop("genero")
                diccionario.pop("autor")
                tatiana.append(diccionario)
        print(tabulate(tatiana, headers="keys", tablefmt="grid"))


def Libr():
        libros = openJSON("libros")
        sara = []
        for diccionario in libros:
                diccionario.pop("descripcion")  
                diccionario.pop("anio_publicacion")
                diccionario.pop("genero")
                diccionario.pop("titulo")
                sara.append(diccionario)
        print(tabulate( sara, headers="keys", tablefmt="grid"))


def nose():
        libros = openJSON("libros")
        juli = []
        for diccionario in libros:
                diccionario.pop("descripcion")  
                diccionario.pop("anio_publicacion")
                diccionario.pop("autor")
                diccionario.pop("titulo")
                juli.append(diccionario)
        print(tabulate(juli, headers="keys", tablefmt="grid"))

