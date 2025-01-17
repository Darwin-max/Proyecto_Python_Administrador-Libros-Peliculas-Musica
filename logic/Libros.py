import json
from tabulate import tabulate
from formula.PARA_TODO import *


libros = openJSON("libros")
def añadirEle():
        print(tabulate(libros, headers="keys", tablefmt="grid"))
        titulo = input("Título: ")
        autor = input("Autor: ")
        genero = input("Género: ")
        año = input("Año: ")
        descripcion =int( input  ("Descripción: "))
        dada = {"titulo": titulo, "autor": autor, "genero": genero, "anio_publicacion": año, "descripcion": descripcion}
        libros.append(dada) # Añadir los datos a la lista de libros

def ver_libros():
        print(tabulate(libros, headers="keys", tablefmt="grid"))