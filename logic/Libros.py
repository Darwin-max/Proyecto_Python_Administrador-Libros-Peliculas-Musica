import json
import tempfile
from tabulate import tabulate
from formula.PARA_TODO import *


libros = openJSON("libros")  # Carga la lista de libros desde un archivo JSON
def añadirEle():
        
        input("Presione Enter para continuar...")
        """
        Añade un nuevo libro a la colección y retorna el libro añadido.
        """
        # Mostrar la colección actual
        print("Colección actual de libros:")
        print(tabulate(libros, headers="keys", tablefmt="grid"))
        # Solicitar datos al usuario
        titulo = input("Título: ").strip()
        autor = input("Autor: ").strip()
        genero = input("Género: ").strip()
        año = input("Año: ").strip()
        descripcion = input("Descripción: ").strip()
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
        return nuevo_libro              # Retornar el libro añadido
libroNuevo = añadirEle()                # Llamar a la función para añadir un libro y guardar el resultado en `libroNuevo`
print("Nuevo libro añadido:")           # Mostrar el nuevo libro añadido en formato tabular
print(tabulate([libroNuevo], headers="keys", tablefmt="grid"))

with tempfile.NamedTemporaryFile(mode='w', delete=False, suffix='.json') as archivo_temp:
        # Guardar los datos JSON en el archivo temporal
        json.dump(libroNuevo, archivo_temp, indent=4)
        print(f"Archivo JSON temporal creado en: {archivo_temp.name}")

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