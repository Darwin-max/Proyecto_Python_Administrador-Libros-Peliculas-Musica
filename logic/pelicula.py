import json
from tabulate import tabulate
from formula.PARA_TODO import *


peliculas = openJSON("peliculas") # Cargar los datos de la lista de películas

def añadirElpeli():         # Añadir elementos a la lista de películas
        print(tabulate(peliculas, headers="keys", tablefmt="grid")) # Mostrar la lista de películas
        titulo = input("Título: ") # Solicitar los datos de la película
        director = input("Director: ") 
        genero = input("Género: ") # si la respuesta no es un numero 
        descripcion = input("Descripción: ") # Crear un diccionario con los datos de la película y el resto de elementos
        dada = {"titulo": titulo, "director": director, "genero": genero, "anio_publicacion": año, "descripcion": descripcion} # Añadir los datos a la lista de películas
        peliculas.append(dada) # Añadir los datos a la lista de películas



def ver_peliculas(): # Buscar una película en la lista de películas

        print(tabulate(peliculas, headers="keys", tablefmt="grid") ) # Mostrar la lista de películas





def peliculas_():
        peliculas = openJSON("pelicula")
        sarey = []
        for dicccionario in peliculas:
                dicccionario.pop("genero")
                dicccionario.pop("año")
                dicccionario.pop("director")
                dicccionario.pop("valoracion")
                dicccionario.pop("descripcion")
                sarey.append(dicccionario)
        print(tabulate(sarey, headers="keys", tablefmt="grid"))
                


def pelicas_():
        pelicula = openJSON("peliculas")
        amor =  []
        for dicccionario in pelicula:
                dicccionario.pop("genero")
                dicccionario.pop("año")
                dicccionario.pop("titulo")
                dicccionario.pop("valoracion")
                dicccionario.pop("descripcion")
                amor.append(dicccionario)
        print(tabulate(    amor, headers="keys", tablefmt="grid"))
                
def masTarde ():
        pelicula = openJSON("peliculas")
        cansado = []
        for dicccionario in pelicula:
                dicccionario.pop("director")
                dicccionario.pop("año")
                dicccionario.pop("titulo")
                dicccionario.pop("valoracion")
                dicccionario.pop("descripcion")
                cansado.append(dicccionario)
        print(tabulate(    cansado, headers="keys", tablefmt="grid"))
                