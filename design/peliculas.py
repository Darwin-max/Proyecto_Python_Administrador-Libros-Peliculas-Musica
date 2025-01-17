from tabulate import tabulate
from logic.pelicula import  peliculas_ , pelicas_
from formula.PARA_TODO import openJSON




def buiscar_pelicula():
    peliculas = openJSON("libros")
    peliculas_()
    print("¿Qué libro deseas buscar?")
    titulo = input("Título: ")
    for peliculas in peliculas:
        if peliculas["titulo"] == titulo:
            print(tabulate([peliculas], headers="keys", tablefmt="grid"))
            break
    else:
        print("No se encontró el pelicula")



def buisr_pelicula():
    peliculas = openJSON("libros")
    pelicas_()
    print("¿Qué libro deseas buscar?")
    director = input("Director: ")
    for peliculas in peliculas:
        if peliculas["director"] == director:
            print(tabulate([peliculas], headers="keys", tablefmt="grid"))
            break
    else:
        print("No se encontró el pelicula")