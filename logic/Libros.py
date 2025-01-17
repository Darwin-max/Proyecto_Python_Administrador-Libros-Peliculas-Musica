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