
from tabulate import tabulate
from formula.PARA_TODO import *



def validar_numero(mensaje):
        while True:
                try:
                        valor = int(input(mensaje))
                        return valor
                except ValueError:
                        print("Por favor, ingrese un número válido.")

libros = openJSON("libros")  # Carga la lista de libros desde un archivo JSON

def añadirEle(ll):
        while True:
                opc = input("ingrese s para añadir un nuevo libro y 0 para terminar: ")
                if opc == '0' :
                        break     
                print(tabulate(libros, headers="keys", tablefmt="grid"))        # Mostrar la colección actual
                nuevo_id = max([libro.get("id", 0) for libro in libros], default=0) + 1 # Generar un ID único para el nuevo libro                nuevo_libro["id"] = nuevo_id    # Añadir el ID al nuevo libro
                id = nuevo_id
                titulo = input("Título: ") .strip()                # Solicitar datos al usuario
                autor = input("Autor: ").strip()
                genero = input("Género: ").strip()
                año = int(input("Año: "))
                descripcion = input("Descripción: ").strip()
                valoracion = int(input("valoracion: "))
                # Crear el nuevo libro como un diccionario
                
                while valoracion < 1 or valoracion > 10:
                        print("Valoración no válida. Debe estar entre 1 y 10.")
                        valoracion = int(input("Valoracion: "))
                
                nuevo_libro = {
                        "id": id,
                        "titulo": titulo,
                        "autor": autor,
                        "genero": genero,
                        "anio_publicacion": año,
                        "descripcion": descripcion,
                        "valoracion" : valoracion
                        }
                        # Añadir el libro a la colección
                ll.append(nuevo_libro)
                return nuevo_libro
                # Retornar el libro añadido
                
                


def ver_libros():
        print(tabulate(libros, headers="keys", tablefmt="grid"))



def Libros():
        libros = openJSON("libros")
        tatiana = []
        for diccionario in libros:
                diccionario.pop("id")
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
                diccionario("id")
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
                diccionario.pop("id")
                diccionario.pop("descripcion")  
                diccionario.pop("anio_publicacion")
                diccionario.pop("autor")
                diccionario.pop("titulo")
                juli.append(diccionario)
        print(tabulate(juli, headers="keys", tablefmt="grid"))

