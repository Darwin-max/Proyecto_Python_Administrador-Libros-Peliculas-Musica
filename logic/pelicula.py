import json
from tabulate import tabulate
from formula.PARA_TODO import *


peliculas = openJSON("peliculas") # Cargar los datos de la lista de películas

def añadirElpeli():         # Añadir elementos a la lista de películas
    print(tabulate(peliculas, headers="keys", tablefmt="grid")) # Mostrar la lista de películas
    titulo = input("Título: ") # Solicitar los datos de la película
    director = input("Director: ") 
    genero = input("Género: ")
    año = input("Año: ")
    descripcion = input("Descripción: ") # Crear un diccionario con los datos de la película y el resto de elementos
    dada = {"titulo": titulo, "director": director, "genero": genero, "anio_publicacion": año, "descripcion": descripcion} # Añadir los datos a la lista de películas
    peliculas.append(dada) # Añadir los datos a la lista de películas



def ver_peliculas(): # Buscar una película en la lista de películas

    print(tabulate(peliculas, headers="keys", tablefmt="grid") ) # Mostrar la lista de películas
