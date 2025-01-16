import json
from tabulate import tabulate
from formula.libros import openJSON
from formula.libros import *


libros = openJSON("libros")
def añadirEle():
        print(tabulate(libros, headers="keys", tablefmt="grid"))
        titulo = input("Título: ")
        autor = input("Autor: ")
        genero = input("Género: ")
        año = input("Año: ")
        dada = {"Título": titulo, "Autor": autor, "Género": genero, "Año": año}
        libros.append(dada)

